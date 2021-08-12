program rfoilrun
    implicit none

    LOGICAL :: file_exists
    CHARACTER(*), PARAMETER :: rfoil_delta_1_file='./output/rfoildata/bl.dst', &
                                rfoil_delta_2_file='./output/rfoildata/bl.tet', &
                                rfoil_results_file='./output/rfoildata/rfoilresults.txt'
    INTEGER, PARAMETER :: nheaderlines=2, ndatapoints=300
    INTEGER :: i, fu, io
    REAL :: x_rfoil(ndatapoints), delta_1_aoa0(ndatapoints), delta_1_aoa10(ndatapoints), delta_1_aoa15(ndatapoints), &
            delta_2_aoa0(ndatapoints), delta_2_aoa10(ndatapoints), delta_2_aoa15(ndatapoints), temp
    
    ! CALL EXECUTE_COMMAND_LINE("mkdir ./output/rfoildata")
    ! CALL EXECUTE_COMMAND_LINE("cmd.exe")
    ! CALL EXECUTE_COMMAND_LINE("rfoil.exe < rfoil_input.txt > ./output/rfoildata/rfoil_output.txt")
    ! CALL EXECUTE_COMMAND_LINE("exit")

    INQUIRE (exist=file_exists, file=rfoil_delta_1_file)
    if (.not. file_exists) then
        print *, 'Error: ',rfoil_delta_1_file,' not found'
    end if

    open (action='read', file=rfoil_delta_1_file, iostat=io, newunit=fu, status='old')
    if (io .NE. 0) then
        print *, 'Error: file open failed'
    end if

    ! skip header lines
    do i = 1, nheaderlines
        read(fu,*,iostat=io)
    end do

    ! read delta* along airfoil surface
    do i = 1, ndatapoints
        read(fu,*,iostat=io) x_rfoil(i), temp, temp, temp, temp, temp, delta_1_aoa0(i), temp, temp, temp, temp, temp, temp, temp, &
                        temp, temp, delta_1_aoa10(i), temp, temp, temp, temp, temp, temp, temp, temp, temp, temp, delta_1_aoa15(i)
    end do

    CLOSE(fu)

    INQUIRE (exist=file_exists, file=rfoil_delta_2_file)
    if (.not. file_exists) then
        print *, 'Error: ',rfoil_delta_2_file,' not found'
    end if

    open (action='read', file=rfoil_delta_2_file, iostat=io, newunit=fu, status='old')
    if (io .NE. 0) then
        print *, 'Error: file open failed'
    end if

    ! skip header lines
    do i = 1, nheaderlines
        read(fu,*,iostat=io)
    end do
    
    ! read theta
    do i = 1, ndatapoints
        READ(fu,*,iostat=io) temp, temp, temp, temp, temp, temp, delta_2_aoa0(i), temp, temp, temp, temp, temp, temp, temp, &
                        temp, temp, delta_2_aoa10(i), temp, temp, temp, temp, temp, temp, temp, temp, temp, temp, delta_2_aoa15(i)
    end do

    CLOSE(fu)

    INQUIRE (exist=file_exists, file=rfoil_results_file)
    if (file_exists) then
        print *, 'Warning: ',rfoil_results_file,' already exists, will be replaced'
    end if
    open(action='write', file=rfoil_results_file, iostat=io, newunit=fu, status='replace')
    do i = 1, ndatapoints
        write(fu,*,iostat=io) x_rfoil(i), delta_1_aoa0(i), delta_2_aoa0(i), delta_1_aoa10(i), delta_2_aoa10(i), delta_1_aoa15(i), &
                                delta_2_aoa15(i)
    end do
    close(fu)


    

end program rfoilrun