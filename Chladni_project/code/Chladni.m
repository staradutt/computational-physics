n=100; % number of grid points in x and y direction 
mu=0.225; % this value of mu is choosen as the ...
%results match quite good with chladnis original
h=2/(n-3); % Distance between grid points
% Set up grid
G=numgrid('S',n+2);%S is square form 
% Define boundary and ghost points
%bl as left edge nodes, gl as left ghost edge nodes and so on 
bl=G(3:n,3);
bt=G(3,3:n)';
br=G(3:n,n); 
bb=G(n,3:n)';
gl=G(3:n,2); 
gt=G(2,3:n)';
gr=G(3:n,n+1);  
gb=G(n+1,3:n)';

%we split L in Lu=lambda*u as L=D2*D1



D1=delsq(G);%discrete laplacian inner which act on u first to get w=-del2u
D2 = D1;%second discrete laplacian to act on w to get the final form 

%we will finally solve LHS=A0*u=D1*D2*u  =  B*u=RHS where RHS gives control
%volume for each node and A0 is the final spatial differential operator


% this modification puts boundary conditions just by changing coefficient 
% of boundary nodes in D2 which we arrive by treating the flux term
% on LHS as values at ghost points which inturn depend on interior grid
%points
D2(bl,bl)=D2(bl,bl)/2; 
D2(br,br)=D2(br,br)/2;
D2(bt,bt)=D2(bt,bt)/2; 
D2(bb,bb)=D2(bb,bb)/2;


% The w value of ghost points are related to u value of neighbouring grid point values
%and nothing else, so that is implemented here:

D1([gl;gr;gt;gb],:)=0;%first set all values to 0 for ghost node rows in D1
%as it doesnt depend on anything other than neghbouring grid values


%these relate the w value of ghost points to neighbouring u values of
%neighbouring grid points

%left
for i=gl(1:end-1)' 
D1([i,i+1],[i,i+1,i+2*n,i+2*n+1])=D1([i,i+1],[i,i+1,i+2*n,i+2*n+1])+(mu-1)/2*[1,-1,-1,1;-1,1,1,-1];
end

%top
for i=gt(1:end-1)' 
D1([i,i+n],[i+n,i,i+n+2,i+2])=D1([i,i+n],[i+n,i,i+n+2,i+2])-(mu-1)/2*[1,-1,-1,1;-1,1,1,-1];
end

%right
for i=gr(1:end-1)' 
D1([i,i+1],[i,i+1,i-2*n,i-2*n+1])=D1([i,i+1],[i,i+1,i-2*n,i-2*n+1])+(mu-1)/2*[1,-1,-1,1;-1,1,1,-1];
end

%bottom
for i=gb(1:end-1)' 
D1([i,i+n],[i+n,i,i+n-2,i-2])=D1([i,i+n],[i+n,i,i+n-2,i-2])-(mu-1)/2*[1,-1,-1,1;-1,1,1,-1];
end

%Compose D1 and D2 to get final 4th order operator which is
%biharmonic for grid points and has incorporated all boundary conditions for edge 
%nodes and ghost w values-interior u value relations in place
A=D2*D1;

%when D1 acts on u value of points we get w value of points, when D2 acts
%on w value of points we get correct LHS

%Actually this A when acts on u values  of grid points can give the correct LHS.
%But in the RHS where we have control volumes defined only for only grid points 
%and not ghost points. Moreover as the u values of ghost points can related to
%u values of grid points using boundary conditions, these ghost points can
%be eliminated to have only grid points.

%boundary conditions to relate u value of ghost points to u value of grid points

A([gl; gr; gt; gb],:)=0;

%left
for i=gl' 
A(i,[i+n,i,i+n-1,i+n+1,i+2*n])=[2*(1+mu), -1, -mu, -mu, -1];
end

%top
for i=gt' 
A(i,[i+1,i,i+1+n,i+1-n,i+2])=[2*(1+mu), -1, -mu, -mu, -1];
end

%right
for i=gr' 
A(i,[i-n,i,i-n-1,i-n+1,i-2*n])=[2*(1+mu), -1, -mu, -mu, -1];
end

%bottom
for i=gb' 
A(i,[i-1,i,i-1+n,i-1-n,i-2])=[2*(1+mu), -1, -mu, -mu, -1];
end


u=G(3:n,3:n);
u=u(:); % this u contains the physical grid points in vectorized form
ghost_nodes=[gl; gr; gt; gb];

%here A matrix of LHS which was to act on full U containing (values at all
%nodes including real grid points and ghost points is reduced to A0 which
%will act only on new U containing only real physical points. This is done
%by taking a schurs complement of A wrt ghost points

A0=A(u,u) - ...
A(u,ghost_nodes)/A(ghost_nodes,ghost_nodes)*A(ghost_nodes,u);
A0=A0/h^2;
%LHS is ready now

%RHS takes care of control volumes (areas to be specific as it is 2D case)
%RHS Bu where B is a diagonal matrix containing coefficient of control
%volume h2 for each node(1 for interior, 1/2 for boundary and 1/4 for
%corners. Since two boundaries share corners 1/2*1/2 happens automatically
%as we do for edges

B=speye(n^2);
B(bl,bl)=B(bl,bl)/2;B(br,br)=B(br,br)/2;
B(bt,bt)=B(bt,bt)/2; B(bb,bb)=B(bb,bb)/2;
B0=B(u,u)*h^2;

% generalized eigenvalue problem A0*u=lambda*B*u
NE=50;%NE specifies number of eigenvalues, can take anything
[U_set,Lambda]=eigs(A0,B0,NE,'SM');%U_set has set of eigenfunctions, Lambda has eigen values
U_set_real=real(U_set);
[y,indices]=sort(diag(Lambda));%sorting the eigen values in increasing order 
%indices is the sorted indices which is used to get later to get
%corresponding eigen functions

y=real(y);

x=[-1:h:1];%setting the grid points from -1 to 1 in steps of h
lamd_expt=[12.4,26.4,36.2,77.5,215,260,310,364,698,819];
lamd_computed_lit=[12.5,26.0,35.6,80.9,235.4,269.3,320.7,375.2,730.0,876.1];
f=fopen('lambda.txt','w');
fprintf(f,'lambda values \n computed by this prog.  computed value from#1  experimental#1\n');


% plotting(first three eigen values come negative so we start from fourth)
t=0;
count=1;
fig=figure;
for i=4:36
subplot(6,6,i) 
ugrid=reshape(U_set_real(:,indices(i)),n-2,n-2);
contour(x,x,ugrid,[0 0],'-k');

axis equal
eival=round(y(i),2);
title (['\lambda=',num2str(eival,'%.1f')])
if eival ~=t && i<=14
    fprintf(f,'%.1f                      %.1f                     %.1f \n', ...
        eival,lamd_computed_lit(count),lamd_expt(count)) ;
    count=count+1;
end
t=eival;
end
saveas(fig,'Chladni.png')
fprintf(f,'\n\n\n\n#1 Pg140, vol 720, Spectral theory and Applications,\n   CRM Summer School July 4–14, 2016, Université Laval, Québec, Canada');
fclose(f);