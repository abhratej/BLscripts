program directoryclean
    implicit none

    CALL EXECUTE_COMMAND_LINE("rm -rf ./*.vtk")
    CALL EXECUTE_COMMAND_LINE("rm -rf ./output/*.txt")
    CALL EXECUTE_COMMAND_LINE("rm -rf ./output/*.tsv")
    CALL EXECUTE_COMMAND_LINE("rm -rf ./output/normalflowfields")
    CALL EXECUTE_COMMAND_LINE("rm -rf ./output/rfoildata/*")
    CALL EXECUTE_COMMAND_LINE("rm -rf ./output/xfoildata/*")

end program directoryclean