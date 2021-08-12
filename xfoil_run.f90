program xfoilrun
    implicit none

    LOGICAL :: file_exists
    CHARACTER(*), PARAMETER :: xfoil_delta_1_bottom_file='./output/xfoildata/xfoil_delta1_theta_bottom.txt', &
                                xfoil_delta_1_top_file='./output/xfoildata/xfoil_delta1_theta_top.txt', &
                                xfoil_results_file='./output/xfoildata/xfoilresults.txt'
    INTEGER, PARAMETER :: nheaderlines=7, ndatalines_top=263, ndatapoints_top=223, ndatalines_bottom=181, ndatapoints_bottom=141, &
                            totaldatapoints=ndatapoints_top+ndatapoints_bottom
    INTEGER :: io, fu, i
    REAL :: x_xfoil(totaldatapoints), delta_1_xfoil(totaldatapoints), delta_2_xfoil(totaldatapoints), temp

    CALL EXECUTE_COMMAND_LINE("mkdir ./output/xfoildata")
    CALL EXECUTE_COMMAND_LINE("xfoil < xfoil_input.txt > ./output/xfoildata/xfoil_output.txt")
    ! CALL EXECUTE_COMMAND_LINE("", wait=.false.)


    ! suction side of airfoil
    INQUIRE (exist=file_exists, file=xfoil_delta_1_top_file)
    if (.not. file_exists) then
        print *, 'Error: ',xfoil_delta_1_top_file,' not found'
    end if

    open (action='read', file=xfoil_delta_1_top_file, iostat=io, newunit=fu, status='old')
    if (io .NE. 0) then
        print *, 'Error: file open failed'
    end if

    ! skip header lines
    do i = 1, nheaderlines
        read(fu,*,iostat=io)
    end do

    ! read delta* along airfoil surface
    do i = 1, ndatapoints_top
        read(fu,*,iostat=io) x_xfoil(i), delta_1_xfoil(i)
    end do

    ! skip points in airfoil wake
    do i = 1, ndatalines_top-ndatapoints_top
        read(fu,*,iostat=io)
    end do

    !skip blank line
    READ(fu,*,iostat=io)

    ! read theta
    do i = 1, ndatapoints_top
        READ(fu,*,iostat=io) temp, delta_2_xfoil(ndatapoints_top+i)
    end do

    CLOSE(fu)

    INQUIRE (exist=file_exists, file=xfoil_delta_1_bottom_file)
    if (.not. file_exists) then
        print *, 'Error: ',xfoil_delta_1_bottom_file,' not found'
    end if

    open (action='read', file=xfoil_delta_1_bottom_file, iostat=io, newunit=fu, status='old')
    if (io .NE. 0) then
        print *, 'Error: file open failed'
    end if

    ! skip header lines
    do i = 1, nheaderlines
        read(fu,*,iostat=io)
    end do

    ! read delta* along airfoil surface
    do i = 1, ndatapoints_bottom
        read(fu,*,iostat=io) x_xfoil(ndatapoints_top+i), delta_1_xfoil(ndatapoints_top+i)
    end do

    ! skip points in airfoil wake
    do i = 1, ndatalines_bottom-ndatapoints_bottom
        read(fu,*,iostat=io)
    end do

    !skip blank line
    READ(fu,*,iostat=io)

    ! read theta
    do i = 1, ndatapoints_bottom
        READ(fu,*,iostat=io) temp, delta_2_xfoil(ndatapoints_top+i)
    end do

    CLOSE(fu)
    

    INQUIRE (exist=file_exists, file=xfoil_results_file)
    if (file_exists) then
        print *, 'Warning: ',xfoil_results_file,' already exists, will be replaced'
    end if
    open(action='write', file=xfoil_results_file, iostat=io, newunit=fu, status='replace')
    do i = 1, totaldatapoints
        write(fu,*,iostat=io) x_xfoil(i), delta_1_xfoil(i), delta_2_xfoil(i)
    end do
    close(fu)


    

end program xfoilrun