package com.reverseengineering;

import java.io.File;
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;


public class AnalysisClient {

    private static final String API_URL =
        "http://127.0.0.1:8000/analysis";

    private final HttpClient client = HttpClient.newBuilder()
        .version(HttpClient.Version.HTTP_1_1).build();

    public String analyze(File file)
        throws IOException, InterruptedException {

            String boundary = "----ReverseEngineeringBoundary";

            byte[] fileBytes = Files.readAllBytes(file.toPath());

            byte[] header = (
                "--" + boundary + "\r\n" +
                "Content-Disposition: form-data; " +
                "name=\"file\"; filename=\"" +
                file.getName() + "\"\r\n" +
                "Content-Type: application/octet-stream\r\n\r\n"
            ).getBytes(StandardCharsets.UTF_8);


            byte[] footer = (
                "\r\n--" + boundary + "--\r\n"
            ).getBytes(StandardCharsets.UTF_8);

            byte[] body = new byte[
                header.length + fileBytes.length + footer.length
            ];

            System.arraycopy(
                header, 0, body, 0, header.length
            );

            System.arraycopy(
                fileBytes, 0, body, header.length,
                fileBytes.length
            );

            System.arraycopy(
                footer, 0, body,
                header.length + fileBytes.length,
                footer.length
            );

            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(API_URL))
                .header(
                    "Content-Type",
                    "multipart/form-data; boundary=" + boundary
                )
                .POST(HttpRequest.BodyPublishers.ofByteArray(body))
                .build();


            HttpResponse<String> response = client.send(
                request,
                HttpResponse.BodyHandlers.ofString()
            );

            if (response.statusCode() != 200) {
                throw new IOException(
                    "Analysis failed. HTTP " +
                    response.statusCode() +
                    ": " + response.body()
                );
            }

            return response.body();
        }
}
