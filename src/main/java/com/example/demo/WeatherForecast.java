package com.example.demo;

import java.util.Date;

public class WeatherForecast {

    private java.util.Date Date;

    private int TemperatureC;

    private int TemperatureF;

    private String Summary;

    public java.util.Date getDate() {
        return Date;
    }

    public void setDate(java.util.Date date) {
        Date = date;
    }

    public int getTemperatureC() {
        return TemperatureC;
    }

    public void setTemperatureC(int temperatureC) {
        TemperatureC = temperatureC;
    }

    public int getTemperatureF() {
        return  32 + (int) (TemperatureC / 0.5556);
    }

    public void setTemperatureF(int temperatureF) {
        TemperatureF = temperatureF;
    }

    public String getSummary() {
        return Summary;
    }

    public void setSummary(String summary) {
        Summary = summary;
    }
}
