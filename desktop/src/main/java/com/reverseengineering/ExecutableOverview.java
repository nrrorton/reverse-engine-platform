package com.reverseengineering;

import com.fasterxml.jackson.databind.JsonNode;

import javafx.geometry.Insets;
import javafx.scene.control.Label;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.VBox;

public class ExecutableOverview extends VBox {

    private final Label nameLabel = new Label();
    private final Label statusLabel = new Label();

    private final Label architectureLabel = new Label();
    private final Label entryPointLabel = new Label();
    private final Label sectionsLabel = new Label();
    private final Label functionsLabel = new Label();
    private final Label hashLabel = new Label();

    public ExecutableOverview() {
        setSpacing(12);
        setPadding(new Insets(15));

        Label title = new Label("Executable Overview");
        title.setStyle(
            "-fx-font-size: 18px; -fx-font-weight: bold;"
        );

        GridPane grid = new GridPane();
        grid.setHgap(25);
        grid.setVgap(10);

        grid.add(new Label("Architecture:"), 0, 0);
        grid.add(architectureLabel, 1, 0);

        grid.add(new Label("Entry Point:"), 0, 1);
        grid.add(entryPointLabel, 1, 1);

        grid.add(new Label("Sections:"), 0, 2);
        grid.add(sectionsLabel, 1, 2);

        grid.add(new Label("Functions:"), 0, 3);
        grid.add(functionsLabel, 1, 3);

        Label hashTitle = new Label("SHA-256:");
        hashLabel.setWrapText(true);

        getChildren().addAll(
            title,
            nameLabel,
            statusLabel,
            grid,
            hashTitle,
            hashLabel
        );
    }

    public void display(JsonNode root) {
        JsonNode executable = root.path("executable");

        nameLabel.setText(
            executable.path("name").asText("Unknown")
        );

        statusLabel.setText(
            "Status: " + root.path("status").asText("Unknown")
        );

        architectureLabel.setText(
            executable.path("architecture").asText("Unknown")
        );

        entryPointLabel.setText(
            executable.path("entry_point_rva").asText("Unknown")
        );

        sectionsLabel.setText(
            String.valueOf(root.path("sections").size())
        );

        functionsLabel.setText(
            String.valueOf(root.path("fucntions").size())
        );

        hashLabel.setText(
            executable.path("sha256").asText("Unknown")
        );
    }
}
