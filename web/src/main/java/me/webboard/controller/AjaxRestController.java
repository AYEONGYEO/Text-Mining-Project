package me.webboard.controller;

import java.util.HashMap;
import java.util.List;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import me.webboard.service.ChartService;

@RestController
public class AjaxRestController {
	
	@Autowired
	private ChartService chartService;
	
	// request GET 방식 일때, 
	// @RequestParam(value = "param", required=false) String param 
	
	@RequestMapping(value="/requestNetworkChart", method=RequestMethod.POST)
	public Object networkChartController(
				HttpServletRequest requst, 
				HttpServletResponse response, 
				@RequestBody String param) throws Exception {

//		System.out.println("******************");
//		System.out.println(param);
		
		List<HashMap<String, Object>> wordList = chartService.searchRealtedWord(param);
		response.setContentType("application/json");
		
//		System.out.println(wordList);
//		System.out.println(wordList.getClass().getName());
		
		return wordList;
	}
	
	@RequestMapping(value="/barchart", method=RequestMethod.POST)
	public Object barChartController(
			@RequestBody String name) throws Exception {
		
//		System.out.println("barchart -----");
//		System.out.println(name);
		
		List<HashMap<String, Object>> barValue = chartService.getBarChartValues(name);
		
//		System.out.println(barValue);
		
		return barValue;
	}
	
	@RequestMapping(value="/articlelink", method=RequestMethod.POST)
	public Object articleLinkController(
				HttpServletRequest requst, 
				HttpServletResponse response,
				@RequestBody String name) throws Exception {
		
//		System.out.println("***********");
		name = "%" + name + "%";
//		System.out.println(name);
		
		List<HashMap<String, Object>> links = chartService.getArticleLinks(name);
		
//		System.out.println( links);
		
		return links;
	}
}

