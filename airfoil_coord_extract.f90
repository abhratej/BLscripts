program airfoilcoord
    implicit none
    
    logical :: file_exists
    real, DIMENSION(:,:), allocatable :: velocity, vorticity, coords
    real :: temp
    INTEGER :: fu, npoints, i, io, lines
    character (len=50), parameter :: airfoil_coord_file="./output/airfoil_coords.txt"

    INQUIRE (exist=file_exists, file='airfoil.tsv')
    if (.not. file_exists) then
        print *, 'Error: airfoil.tsv not found'
    end if

    open (action='read', file='airfoil.tsv', iostat=io, newunit=fu, status='old')
    if (io .NE. 0) then
        print *, 'Error: file open failed'
    end if

    lines=0
    read(fu,*,iostat=io) !skip header line
    do
        if ( io .ne. 0 ) exit 
        read(fu,*,iostat=io)
        lines = lines+1
    end do
    rewind(fu)
    npoints=lines-1

    ALLOCATE(coords(npoints,3), vorticity(npoints,3), velocity(npoints,3))

    read(fu,*,iostat=io) !skip header line
    do i=1,npoints
        if ( io .ne. 0 ) exit 
        read (fu,*,iostat=io) temp, temp, temp, temp, temp, temp, temp, temp, temp, temp, temp, velocity(i,1), velocity(i,2), &
        velocity(i,3), vorticity(i,1), vorticity(i,2), vorticity(i,3), coords(i,1), coords(i,2), coords(i,3)
    enddo
    CLOSE(fu)
    
    INQUIRE (exist=file_exists, file=airfoil_coord_file)
    if (file_exists) then
        print *, 'Warning: airfoil_coords.txt already exists, will be replaced'
    end if
    open(action='write', file=airfoil_coord_file, iostat=io, newunit=fu, status='replace')
    write(fu,*,iostat=io) npoints
    do i = 1, npoints
        write(fu,*,iostat=io) coords(i,:)
    end do
    close(fu)

endprogram airfoilcoord