program airfoilgeometry
    implicit none
    
    logical :: file_exists
    real, allocatable :: coords(:,:), l(:), normal(:,:), dx(:), dy(:)
    real :: temp
    INTEGER :: fu, npoints, i, io, lines
    character (*), parameter :: paraview_airfoil_surface_file='./output/airfoil.tsv',&
                                airfoil_coord_file="./output/airfoil_coords.txt",&
                                airfoil_norm_file='./output/airfoil_normals.txt'

    CALL EXECUTE_COMMAND_LINE("mkdir ./output")
    CALL EXECUTE_COMMAND_LINE("pvpython ./airfoil_surface_paraview.py")

    INQUIRE (exist=file_exists, file=paraview_airfoil_surface_file)
    if (.not. file_exists) then
        print *, 'Error: ',paraview_airfoil_surface_file,' not found'
    end if

    open (action='read', file=paraview_airfoil_surface_file, iostat=io, newunit=fu, status='old')
    if (io .NE. 0) then
        print *, 'Error: cannot open ',paraview_airfoil_surface_file
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

    ALLOCATE(coords(npoints,3),l(npoints), normal(npoints,2), dx(npoints), dy(npoints))

    !--------------------------------------------------------------------------------------------------------------------
    ! IMPORTANT: Check if headers of airfoil.tsv file are in same order as below, else change read routine accordingly  |
    !--------------------------------------------------------------------------------------------------------------------
    ! "Pressure" "Velocity:0" "Velocity:1" "Velocity:2" "Turb_Kin_Energy" "Omega" "Pressure_Coefficient" "Density"      |
    ! "Laminar_Viscosity" "Skin_Friction_Coefficient:0" "Skin_Friction_Coefficient:1" "Skin_Friction_Coefficient:2"     |
    ! "Heat_Flux" "Y_Plus" "Eddy_Viscosity" "Points:0" "Points:1" "Points:2"                                            |
    !--------------------------------------------------------------------------------------------------------------------

    ! read airfoil.tsv file
    read(fu,*,iostat=io) !skip header line
    do i=1,npoints
        if ( io .ne. 0 ) exit 
        read (fu,*,iostat=io) temp, temp, temp, temp, temp, temp, temp, temp, temp, temp, temp, temp, temp, temp, temp, &
                                coords(i,1), coords(i,2), coords(i,3)
    end do
    CLOSE(fu)
    
    ! write airfoil coordinates file
    INQUIRE (exist=file_exists, file=airfoil_coord_file)
    if (file_exists) then
        print *, 'Warning: ',airfoil_coord_file,' already exists, will be replaced'
    end if
    open(action='write', file=airfoil_coord_file, iostat=io, newunit=fu, status='replace')
    do i = 1, npoints
        write(fu,*,iostat=io) coords(i,:)
    end do
    close(fu)

    ! Compute normals in cartesian notation: normal(:,1) is x coefficient and normal(:,2) is y coefficient
    do i = 1, npoints
        if (i.lt.npoints) then
            l(i) = sqrt((coords(i+1,2) - coords(i,2))**2.0 + (coords(i+1,1) - coords(i,1))**2.0)
            dx(i) = coords(i+1,1) - coords(i,1)
            dy(i) = coords(i+1,2) - coords(i,2)
            normal(i,1) = dx(i)/l(i)
            normal(i,2) = dy(i)/l(i)
        else if (i.eq.npoints) then
            l(i) = sqrt((coords(1,2) - coords(i,2))**2.0 + (coords(1,1) - coords(i,1))**2.0)
            dx(i) = coords(1,1) - coords(i,1)
            dy(i) = coords(1,2) - coords(i,2)
            normal(i,1) = dx(i)/l(i)
            normal(i,2) = dy(i)/l(i)
        end if
    end do

    ! Write airfoil normals file
    INQUIRE (exist=file_exists, file=airfoil_norm_file)
    if (file_exists) then
        print *, 'Warning: ',airfoil_norm_file,' already exists, will be replaced'
    end if
    open(action='write', file=airfoil_norm_file, iostat=io, newunit=fu, status='replace')
    ! write(fu,*,iostat=io) npoints
    do i = 1, npoints
        write(fu,*,iostat=io) coords(i,1), coords(i,2), normal(i,1), normal(i,2)
    end do
    close(fu)


end program airfoilgeometry