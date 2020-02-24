package com.example.demo;

import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Random;

@RestController
@RequestMapping("/")
public class WeatherForecastController {


    /*
    @RequestMapping("/*")
    public String getPage() {
        return "redirect:/resources/static/index.html";
    }
*/
    @RequestMapping(path = "/weatherforecast", method = RequestMethod.GET, produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<List<WeatherForecast>> listAllAppointment() {

        String[] Summaries = {
            "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
        };

        List<WeatherForecast> weatherForecastList =new ArrayList<>();
        WeatherForecast weatherForecast = new WeatherForecast();
        weatherForecast.setDate(new Date());
        weatherForecast.setTemperatureC(59);
        weatherForecast.setSummary(Summaries[0]);
        weatherForecastList.add(weatherForecast);

        return new ResponseEntity<>(weatherForecastList, HttpStatus.OK);
    }

}
