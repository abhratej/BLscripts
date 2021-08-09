program directoryclean
    implicit none

    CHARACTER(*), PARAMETER :: casefolder="/home/abhratej/workdir/Inc_Turb_NACA0012/SA/Re6e6/AoA10"

    CALL EXECUTE_COMMAND_LINE(("mkdir "//casefolder//"/blresults/"))
    CALL EXECUTE_COMMAND_LINE(("cp -r ./output/rfoildata/* "//casefolder//"/blresults/"))
    CALL EXECUTE_COMMAND_LINE(("cp -r ./output/*.txt "//casefolder//"/blresults/"))
    CALL EXECUTE_COMMAND_LINE("rm -rf ./*.vtk")
    CALL EXECUTE_COMMAND_LINE("rm -rf ./output/*.txt")
    CALL EXECUTE_COMMAND_LINE("rm -rf ./output/*.tsv")
    CALL EXECUTE_COMMAND_LINE("rm -rf ./output/normalflowfields")
    CALL EXECUTE_COMMAND_LINE("rm -rf ./output/rfoildata/*")
    CALL EXECUTE_COMMAND_LINE("rm -rf ./output/xfoildata/*")
    CALL EXECUTE_COMMAND_LINE("rm -rf ./fortran_compile_files/*")


end program directoryclean