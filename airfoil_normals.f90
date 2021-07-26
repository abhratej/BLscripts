program airfoilnormal
    implicit none

    CHARACTER(len=50), PARAMETER :: airfoil_coord_file='./output/airfoil_coords.txt', &
                                    airfoil_norm_file='./output/airfoil_normals.txt'
    LOGICAL :: file_exists
    INTEGER :: fu, io, npoints, i
    REAL, ALLOCATABLE :: x(:), y(:), l(:), normal(:,:), dx(:), dy(:)
    
    ! Read airfoil coordinates file
    INQUIRE(exist=file_exists, file=airfoil_coord_file)
    if ( .not. file_exists ) then
        print *, 'Error: airfoil_coords.txt not found in output folder'
    end if
    OPEN(action='read', file=airfoil_coord_file, iostat=io, newunit=fu,status='old')
    READ(fu,*,iostat=io) npoints
    ALLOCATE(x(npoints), y(npoints), l(npoints), normal(npoints,2), dx(npoints), dy(npoints))
    do i = 1, npoints
        READ(fu,*,iostat=io) x(i), y(i)
    end do
    CLOSE(fu)

    ! Compute normals in cartesian notation: normal(:,1) is x coefficient and normal(:,2) is y coefficient
    do i = 1, npoints
        if ( i .lt. npoints ) then
            l(i) = sqrt((y(i+1) - y(i))**2.0 + (x(i+1) - x(i))**2.0)
            dx(i) = x(i+1) - x(i)
            dy(i) = y(i+1) - y(i)
            normal(i,1) = dx(i)/l(i)
            normal(i,2) = dy(i)/l(i)
        else if ( i .eq. npoints ) then
            l(i) = sqrt((y(1) - y(i))**2.0 + (x(1) - x(i))**2.0)
            dx(i) = x(1) - x(i)
            dy(i) = y(1) - y(i)
            normal(i,1) = dx(i)/l(i)
            normal(i,2) = dy(i)/l(i)
        end if
        
    end do

    ! Write airfoil normals file
    INQUIRE (exist=file_exists, file=airfoil_norm_file)
    if (file_exists) then
        print *, 'Warning: airfoil_normals.txt already exists, will be replaced'
    end if
    open(action='write', file=airfoil_norm_file, iostat=io, newunit=fu, status='replace')
    ! write(fu,*,iostat=io) npoints
    do i = 1, npoints
        write(fu,*,iostat=io) x(i), y(i), normal(i,:)
    end do
    close(fu)

end program airfoilnormal

