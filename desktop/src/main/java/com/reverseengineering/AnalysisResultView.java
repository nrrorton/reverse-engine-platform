package com.reverseengineering;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import javafx.scene.control.TreeItem;
import javafx.scene.control.TreeView;

public class AnalysisResultView extends TreeView<String> {

    private final ObjectMapper mapper = new ObjectMapper();

    public AnalysisResultView() {
        setShowRoot(true);
    }

    public void display(String json) throws Exception {
        JsonNode rootNode = mapper.readTree(json);

        TreeItem<String> rootItem =
            new TreeItem<>("Analysis Results");

            buildTree(rootNode, rootItem);

            rootItem.setExpanded(true);
            setRoot(rootItem);
    }

    private void buildTree(
        JsonNode node,
        TreeItem<String> parent) {

            if (node.isObject()) {
                node.properties().forEach(entry -> {
                    TreeItem<String> child =
                        new TreeItem<>(entry.getKey());

                    parent.getChildren().add(child);
                    buildTree(entry.getValue(), child);
                });
            } else if (node.isArray()) {
                for (int i = 0; i < node.size(); i++) {
                    TreeItem<String> child =
                        new TreeItem<>("[" + i + "]");

                    parent.getChildren().add(child);
                    buildTree(node.get(i), child);
                }
            } else {
                parent.setValue(
                    parent.getValue() + ": " + node.asText()
                );
            }
        } 
}
