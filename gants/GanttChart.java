import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.chart.CategoryAxis;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.StackedBarChart;
import javafx.scene.chart.XYChart;
import javafx.scene.control.Tooltip;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

public class GanttChart extends Application {

    private static final String CSS_PATH = "gantt-style.css";

    class Phase {
        String name;
        LocalDate start, end;
        String color;
        String[] tasks;
        LocalDate[] taskDates;

        Phase(String name, String start, String end, String color, String[] tasks, String[] taskDates) {
            this.name = name;
            this.start = LocalDate.parse(start);
            this.end = LocalDate.parse(end);
            this.color = color;
            this.tasks = tasks;
            this.taskDates = new LocalDate[taskDates.length];
            for (int i = 0; i < taskDates.length; i++) {
                this.taskDates[i] = LocalDate.parse(taskDates[i]);
            }
        }
    }

    private Phase[] phases = {
        new Phase("Foundation", "2024-01-01", "2024-06-30", "#4E79A7",
            new String[]{"Finalize workflows", "Develop MVP"},
            new String[]{"2024-01-01", "2024-04-01"}),

        new Phase("Scaling", "2024-07-01", "2025-06-30", "#59A14F",
            new String[]{"Hire analysts", "Secure contracts"},
            new String[]{"2024-07-01", "2024-10-01"}),

        new Phase("Industrialization", "2025-07-01", "2026-12-31", "#F28E2B",
            new String[]{"Automate pipelines", "Global expansion"},
            new String[]{"2025-07-01", "2026-01-01"})
    };

    private String[] milestones = {
        "Pilot clients (Jun 2024)", "ISO Cert (Dec 2024)",
        "EU Contract (Jun 2025)", "SaaS Launch (Dec 2025)"
    };
    private LocalDate[] milestoneDates = {
        LocalDate.parse("2024-06-30"), LocalDate.parse("2024-12-31"),
        LocalDate.parse("2025-06-30"), LocalDate.parse("2025-12-31")
    };

    @Override
    public void start(Stage stage) {
        CategoryAxis yAxis = new CategoryAxis();
        NumberAxis xAxis = new NumberAxis();
        xAxis.setLabel("Timeline (Months from start)");

        StackedBarChart<Number, String> chart = new StackedBarChart<>(xAxis, yAxis);
        chart.setTitle("Quantum Tech Spin-Off Development Plan");
        chart.setLegendVisible(false);

        // Add phases
        for (Phase phase : phases) {
            long phaseDays = ChronoUnit.DAYS.between(phase.start, phase.end);

            XYChart.Series<Number, String> series = new XYChart.Series<>();
            series.setName(phase.name);

            XYChart.Data<Number, String> data = new XYChart.Data<>(
                phaseDays, phase.name);
            data.nodeProperty().addListener((obs, oldNode, newNode) -> {
                if (newNode != null) {
                    newNode.setStyle("-fx-bar-fill: " + phase.color + ";");
                    Tooltip.install(newNode, new Tooltip(phase.name + "\n" +
                        phase.start + " to " + phase.end));
                }
            });
            series.getData().add(data);
            chart.getData().add(series);
        }

        // Add milestones
        XYChart.Series<Number, String> milestoneSeries = new XYChart.Series<>();
        for (int i = 0; i < milestones.length; i++) {
            long daysFromStart = ChronoUnit.DAYS.between(
                LocalDate.parse("2024-01-01"), milestoneDates[i]);

            XYChart.Data<Number, String> data = new XYChart.Data<>(
                daysFromStart, "Milestones");
            data.nodeProperty().addListener((obs, oldNode, newNode) -> {
                if (newNode != null) {
                    newNode.setStyle("-fx-bar-fill: #E15759; -fx-shape: \"M0,0 L10,0 L5,10 Z\";");
                    Tooltip.install(newNode, new Tooltip(milestones[i]));
                }
            });
            milestoneSeries.getData().add(data);
        }
        chart.getData().add(milestoneSeries);

        VBox vbox = new VBox(chart);
        Scene scene = new Scene(vbox, 800, 400);
        scene.getStylesheets().add(getClass().getResource(CSS_PATH).toExternalForm());

        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}.
