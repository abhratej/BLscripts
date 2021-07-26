program airfoilcoord
    implicit none
    
    logical :: file_exists

    INQUIRE (exist=file_exists, file='airfoil.csv')

    if (.not. file_exists) then
        print , 'Error: airfoil.csv not found'
    end if

    

end program airfoilcoord