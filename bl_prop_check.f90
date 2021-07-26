program blprops
    implicit none

    CHARACTER(*), PARAMETER :: normal_flow_file_prefix='./output/normalflowfields/flow_along_normal_point', &
                                    bl_edge_file='./output/bl_edge.txt'
    ! CHARACTER(len=6) :: point_num_str
    CHARACTER(100) :: normal_flow_file
    LOGICAL :: file_exists
    INTEGER :: fu, io, lines, ngridpoints, i, bl_index, airfoil_point_num!, allostat
    INTEGER, PARAMETER :: airfoilpoints=512 ! 512 points on the airfoil, change according to mesh
    REAL :: temp, Re, bl_edge(airfoilpoints,3)
    REAL, ALLOCATABLE :: vort_mag(:), coords(:,:)

    ! IMPORTANT: Check if paraview data file has same headers as below, else change read routine accordingly
    ! "Nu_Tilde" "Pressure_Coefficient" "Density" "Laminar_Viscosity" "Skin_Friction_Coefficient:0" "Skin_Friction_Coefficient:1"
    ! "Skin_Friction_Coefficient:2" "Heat_Flux" "Y_Plus" "Eddy_Viscosity" "Pressure" "Velocity:0" "Velocity:1" "Velocity:2" 
    ! "vorticity:0" "vorticity:1" "vorticity:2" "velocity_magnitude" "vorticity_magnitude" "Points:0" "Points:1" "Points:2"



    do airfoil_point_num = 1, airfoilpoints
        
        ! Read normal data file
        normal_flow_file = TRIM(normal_flow_file_prefix)//trim(str(airfoil_point_num))//'.tsv'
        INQUIRE(exist=file_exists, file=normal_flow_file)
        if ( .not. file_exists ) then
            print *, 'Error: '//TRIM(normal_flow_file)//' not found in output/normalflowfields folder'
        else
            print *, 'File '//TRIM(normal_flow_file)//' found'
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
        print *, 'There are '//trim(str(ngridpoints))//' grid points'
    
        ALLOCATE(vort_mag(ngridpoints), coords(ngridpoints,3))
        print *, 'Variables allocated'
        
        read(fu,*,iostat=io) !skip header line
        do i = 1, ngridpoints
            if ( io .ne. 0 ) exit 
            read (fu,*,iostat=io) temp, temp, temp, temp, temp, temp, temp, temp, temp, temp, temp, temp, temp, temp, temp, temp, &
                                    temp,  temp, vort_mag(i), coords(i,1), coords(i,2), coords(i,3)
        end do
        print *, 'Values assigned to variables'
       
        Re = 6.00e6
        bl_index = 0
        do i = 1, ngridpoints-1
            bl_index = i
            if (vort_mag(i).lt.1.00 .and. vort_mag(i).gt.vort_mag(i+1)) exit
        end do

        if (bl_index .ne. 0) then
            print *, 'BL edge found'
            print *, 'BL index = ', bl_index
        else
            print *, 'Error: BL edge not found'
        end if
        
        bl_edge(airfoil_point_num,1) = coords(bl_index,1)
        bl_edge(airfoil_point_num,2) = coords(bl_index,2)
        bl_edge(airfoil_point_num,3) = coords(bl_index,3)
        print *, 'BL edge assigned to variable'

        DEALLOCATE(vort_mag, coords)

    end do
    
! Write airfoil normals file
    INQUIRE (exist=file_exists, file=bl_edge_file)
    if (file_exists) then
        print *, 'Warning: bl_edge.txt already exists, will be replaced'
    end if
    open(action='write', file=bl_edge_file, iostat=io, newunit=fu, status='replace')
    do airfoil_point_num = 1, airfoilpoints
        write(fu,*,iostat=io) bl_edge(airfoil_point_num,1), bl_edge(airfoil_point_num,2), bl_edge(airfoil_point_num,3)
    end do
    close(fu)

contains

character(len=20) function str(k)
!   "Convert an integer to string."
    integer, intent(in) :: k
    write (str, *) k
    str = adjustl(str)
end function str

end program blprops