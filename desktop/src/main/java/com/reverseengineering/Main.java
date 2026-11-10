package com.reverseengineering;

import java.io.File;
import java.util.List;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.input.Dragboard;
import javafx.scene.input.TransferMode;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;


public class Main extends Application {

    private final AnalysisClient analysisClient =
        new AnalysisClient();
    
    @Override
    public void start(Stage stage) {

        Label label = new Label(
            "Drop PE executable here"
        );

        StackPane root = new StackPane(label);

        root.setStyle(
            "-fx-border-color: #888888;" +
            "-fx-border-width: 2;" +
            "-fx-border-style: dashed;" +
            "-fx-padding: 40;"
        );

        root.setOnDragOver(event -> {
            Dragboard dragboard = event.getDragboard();

            if (dragboard.hasFiles()) {
                event.acceptTransferModes(
                    TransferMode.COPY
                );
            }
            event.consume();
        });

        root.setOnDragDropped(event -> {
            Dragboard dragboard = event.getDragboard();
            boolean success = false;

            if (dragboard.hasFiles()) {
                List<File> files = dragboard.getFiles();

                if (files.size() == 1) {
                    File file = files.get(0);

                    label.setText(
                        "Selected: " + file.getName()
                    );

                    System.out.println(
                        "Selected file: " +
                        file.getAbsolutePath()
                    );

                    label.setText("Analyzing: " + file.getName());

                    Thread analysisThread = new Thread(() -> {
                        try {
                            String json = analysisClient.analyze(file);
                            System.out.println(json);
                            Platform.runLater(() -> {
                                label.setText(
                                    "Analysis complete: " + file.getName()
                                );
                            });
                        } catch (Exception exception) {
                            exception.printStackTrace();

                            Platform.runLater(() -> {
                                label.setText(
                                    "Analysis failed: " +
                                    exception.getMessage()
                                );
                            });
                        }
                    });
                    analysisThread.setDaemon(true);
                    analysisThread.start();
                    success = true;
                }
            }
            event.setDropCompleted(success);
            event.consume();
        });

        Scene scene = new Scene(root, 900, 600);

        stage.setTitle("Reverse Engineering Platform");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
