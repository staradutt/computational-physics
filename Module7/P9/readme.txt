The program creates frames for L=10 i.e 10x10 grid, tau=1000 in the folder named 'frames'.
The frames are stitched using ffmpeg in terminal.
The following command does that:
ffmpeg -i dim%d.png -c:v libx264 animation.mp4
