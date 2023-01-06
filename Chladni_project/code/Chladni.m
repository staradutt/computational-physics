n = 100; % Number of points per direction (includes ghost points)
mu = 0.225; % Material constant
h = 2/(n-3); % Distance between grid points
M = 90; % Number of eigenvalues desired
% Set up grid
G = numgrid('S',n+2); D = delsq(G);



% Define boundary and ghost points
bl = G(3:n,3); br = G(3:n,n); bt = G(3,3:n)'; bb = G(n,3:n)';
gl = G(3:n,2); gr = G(3:n,n+1); gt = G(2,3:n)'; gb = G(n+1,3:n)';
% Initialize N and L to the discrete Laplacian
L = D; N = D;
% Correct outer Laplacian N for boundary conditions
N(bl,bl) = N(bl,bl)/2; N(br,br) = N(br,br)/2;
N(bt,bt) = N(bt,bt)/2; N(bb,bb) = N(bb,bb)/2;
% Trick: Modify the stencil in L at the ghost points to approximate
% ddu/dndt, which gives the correct boundary conditions
L([gl;gr;gt;gb],:) = 0;
for i=gl(1:end-1)' %left
L([i,i+1],[i,i+1,i+2*n,i+2*n+1]) = ...
L([i,i+1],[i,i+1,i+2*n,i+2*n+1]) + (mu-1)/2*[1,-1,-1,1;-1,1,1,-1];
end
for i=gr(1:end-1)' %right
L([i,i+1],[i,i+1,i-2*n,i-2*n+1]) = ...
L([i,i+1],[i,i+1,i-2*n,i-2*n+1]) + (mu-1)/2*[1,-1,-1,1;-1,1,1,-1];
end
for i=gt(1:end-1)' %top
L([i,i+n],[i+n,i,i+n+2,i+2]) = ...
L([i,i+n],[i+n,i,i+n+2,i+2]) - (mu-1)/2*[1,-1,-1,1;-1,1,1,-1];
end
for i=gb(1:end-1)' %bottom
L([i,i+n],[i+n,i,i+n-2,i-2]) = ...
L([i,i+n],[i+n,i,i+n-2,i-2]) - (mu-1)/2*[1,-1,-1,1;-1,1,1,-1];
end
% Compose N and L to get 4th order operator
A = N*L;
% Use boundary conditions to eliminate ghost points
A([gl; gr; gt; gb],:) = 0;
for i=gl' %left
A(i,[i+n,i,i+n-1,i+n+1,i+2*n]) = [2*(1+mu), -1, -mu, -mu, -1];
end
for i=gr' %right
A(i,[i-n,i,i-n-1,i-n+1,i-2*n]) = [2*(1+mu), -1, -mu, -mu, -1];
end
for i=gt' %top
A(i,[i+1,i,i+1+n,i+1-n,i+2]) = [2*(1+mu), -1, -mu, -mu, -1];
end
for i=gb' %bottom
A(i,[i-1,i,i-1+n,i-1-n,i-2]) = [2*(1+mu), -1, -mu, -mu, -1];
end
% Eliminate ghost points
phys = G(3:n,3:n); phys = phys(:); % put all physical nodes in a vector
ghost = [gl; gr; gt; gb];
A0 = A(phys,phys) - A(phys,ghost)/A(ghost,ghost)*A(ghost,phys);
% RHS: take into account half cells and quarter cells
B = speye(n^2);
B(bl,bl) = B(bl,bl)/2; B(br,br) = B(br,br)/2;
B(bt,bt) = B(bt,bt)/2; B(bb,bb) = B(bb,bb)/2;
B0 = B(phys,phys);
% Generalized eigenvalue problem
[V,Lambda] = eigs(A0/h^4,B0,M,'SM');
ty=real(V);
[y,p] = sort(diag(Lambda));
x=[-1:2/(n-3):1];
% plot Chladni figures
tilplot=tiledlayout(3,3)
for i=[6,25,29,33,38,45,51,54,58]
nexttile 
contour(x,x,reshape(ty(:,p(i)),n-2,n-2),[0 0]);
axis equal
set(gca,'XTick',[])
set(gca,'YTick',[])
end
exportgraphics(tilplot,"chladni.png")
