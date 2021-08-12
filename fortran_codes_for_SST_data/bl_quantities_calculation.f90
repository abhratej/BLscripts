program blquantities
    implicit none

    CHARACTER(*), PARAMETER :: normal_flow_file_prefix='./output/normalflowfields/flow_along_normal_point', &
                                    bl_quantities_file='./output/bl_quantities.txt'
    CHARACTER(100) :: normal_flow_file
    LOGICAL :: file_exists
    INTEGER :: fu, io, lines, ngridpoints, i, bl_index, airfoil_point_num
    INTEGER, PARAMETER :: airfoilpoints=512 ! 512 points on the airfoil, change according to mesh
    REAL :: temp, Re, bl_edge(airfoilpoints,3), u_edge, delta(airfoilpoints), delta_1(airfoilpoints), delta_2(airfoilpoints), &
                delta_3(airfoilpoints)
    REAL, ALLOCATABLE :: vort_mag(:), coords(:,:), velocity(:,:), vel_mag(:), cp(:)

    ! Extracting flowfield data along surface normals
    CALL EXECUTE_COMMAND_LINE("mkdir ./output/normalflowfields")
    CALL EXECUTE_COMMAND_LINE("pvpython ./normal_flowfield_paraview.py")

    !------------------------------------------------------------------------------------------------------------------------------
    ! IMPORTANT: Check if paraview data file has same headers as below, else change read routine accordingly                      |
    !------------------------------------------------------------------------------------------------------------------------------
    ! "Turb_Kin_Energy" "Omega" "Pressure_Coefficient" "Density" "Laminar_Viscosity" "Skin_Friction_Coefficient:0"                |
    ! "Skin_Friction_Coefficient:1" "Skin_Friction_Coefficient:2" "Heat_Flux" "Y_Plus" "Eddy_Viscosity" "Pressure" "Velocity:0"   |
    ! "Velocity:1" "Velocity:2" "vorticity:0" "vorticity:1" "vorticity:2" "velocity_magnitude" "vorticity_magnitude" "Points:0"   |
    ! "Points:1" "Points:2"                                                                                                       |
    !------------------------------------------------------------------------------------------------------------------------------

    do airfoil_point_num = 1, airfoilpoints
        
        ! Read normal data file
        normal_flow_file = TRIM(normal_flow_file_prefix)//trim(str(airfoil_point_num))//'.tsv'
        INQUIRE(exist=file_exists, file=normal_flow_file)
        if ( .not. file_exists ) then
            print *, 'Error: '//TRIM(normal_flow_file)//' not found in output/normalflowfields folder'
        ! else
        !     print *, 'File '//TRIM(normal_flow_file)//' found'
        end if
        OPEN(action='read', file=normal_flow_file, iostat=io, newunit=fu,status='old')
        
        lines=0
        read(fu,*,iostat=io) !skip header line
        do
            if ( io .ne. 0 ) exit 
            read(fu,*,iostat=io)
            lines = lines+1
        end do
        rewind(fu)
        ngridpoints=lines-1
        ! print *, 'There are '//trim(str(ngridpoints))//' grid points'
    
        ALLOCATE(vort_mag(ngridpoints), coords(ngridpoints,3), velocity(ngridpoints,3), vel_mag(ngridpoints), cp(ngridpoints))
        ! print *, 'Variables allocated'
        
        read(fu,*,iostat=io) !skip header line
        do i = 1, ngridpoints
            if ( io .ne. 0 ) exit 
            read (fu,*,iostat=io) temp, temp, cp(i), temp, temp, temp, temp, temp, temp, temp, temp, temp, velocity(i,1), &
                                velocity(i,2), velocity(i,3), temp, temp, temp, vel_mag(i), vort_mag(i), coords(i,1), &
                                coords(i,2), coords(i,3)
        end do
        ! print *, 'Values assigned to variables'
       
        Re = 6.00e6
        bl_index = 0
        do i = 1, ngridpoints-1
            bl_index = i
            ! if ((vort_mag(i)/52.1573).lt.0.0001 .and. vort_mag(i).gt.vort_mag(i+1)) exit
            if ((vort_mag(i)/52.1573).lt.0.001) exit

        end do

        if (bl_index .eq. 0) then
            print *, 'Error: BL edge not found'
        ! else
        !     print *, 'BL edge found'
        !     print *, 'BL index = ', bl_index
        end if
        

        bl_edge(airfoil_point_num,:) = coords(bl_index,:)
        ! print *, 'BL edge assigned to variable'

        delta(airfoil_point_num) = SQRT((coords(bl_index,1)-coords(1,1))**2.0 + (coords(bl_index,2)-coords(1,2))**2.0 + &
        (coords(bl_index,3)-coords(1,3))**2.0)

        u_edge = vel_mag(bl_index+1)
        ! u_edge = sqrt(1.0 - min(1.0,cp(1)))

        delta_1(airfoil_point_num) = 0.0
        delta_2(airfoil_point_num) = 0.0
        delta_3(airfoil_point_num) = 0.0

        do i = 1, bl_index
            delta_1(airfoil_point_num) = delta_1(airfoil_point_num) + ((1.0 - (vel_mag(i)/u_edge))*(ABS(coords(i+1,2)-coords(i,2))))
            delta_2(airfoil_point_num) = delta_2(airfoil_point_num) + ((vel_mag(i)/u_edge) * (1.0 - (vel_mag(i)/u_edge)) * &
                                            (ABS(coords(i+1,2)-coords(i,2))))
            delta_3(airfoil_point_num) = delta_3(airfoil_point_num) + ((vel_mag(i)/u_edge) * (1.0 - ((vel_mag(i)/u_edge)**2.0)) * &
                                            (ABS(coords(i+1,2)-coords(i,2))))
        end do

        DEALLOCATE(vort_mag, coords, velocity, vel_mag, cp)

    end do
    
! Write bl quantities file
    INQUIRE (exist=file_exists, file=bl_quantities_file)
    if (file_exists) then
        print *, 'Warning: bl_quantities.txt already exists, will be replaced'
    end if
    open(action='write', file=bl_quantities_file, iostat=io, newunit=fu, status='replace')
    do airfoil_point_num = 1, airfoilpoints
        write(fu,*,iostat=io) bl_edge(airfoil_point_num,1), bl_edge(airfoil_point_num,2), bl_edge(airfoil_point_num,3), &
                                delta(airfoil_point_num), delta_1(airfoil_point_num), delta_2(airfoil_point_num), &
                                delta_3(airfoil_point_num)
    end do
    close(fu)

contains

character(len=20) function str(k)
!   "Convert an integer to string."
    integer, intent(in) :: k
    write (str, *) k
    str = adjustl(str)
end function str

end program blquantities