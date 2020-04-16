package me.webboard.controller;

import java.util.HashMap;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;

import me.webboard.mapper.ChartMapper;
import me.webboard.model.ChartVO;
import me.webboard.service.ChartService;

@Controller
@EnableAutoConfiguration
public class ChartController {
	
	@Autowired
	private ChartMapper mapper;
	
	@Autowired
	private ChartService chartService;
	
	  // tf 데이터 가져오기 테스트
	  @RequestMapping("/ccc") 
	  public ModelAndView show() throws Exception {
	  
		  ModelAndView mv = new ModelAndView(); 
		  List<ChartVO> chartList =  mapper.showChart();
	  
		  mv.setViewName("charts"); 
		  mv.addObject("chartList", chartList);
	  
		  return mv; 
	  }
	  
	  @RequestMapping("/data")
	  @ResponseBody
	  public List<ChartVO> getWordJson() {
		  
		  List<ChartVO> words = chartService.getWordJson();
		  
		  return words;
	  }
	  
	  @RequestMapping("/olympic")
	  public ModelAndView olympicMain() throws Exception {
		  
		  ModelAndView mv = new ModelAndView();
		  List<ChartVO> words = chartService.getWordJson();
		  
		  mv.setViewName("index");
		  mv.addObject("words", words);
		  
		  return mv;
	  }
	  
	  @RequestMapping("/top10")
	  public ModelAndView olympicTop10() throws Exception {
		  
		  ModelAndView mv = new ModelAndView();
		  List<HashMap<String, Object>> topten = chartService.getTopTen();
		  
		  mv.setViewName("top10");
		  mv.addObject("topten", topten);
		  
		  return mv;
	  }
	  
	  @RequestMapping("tf")
	  public ModelAndView olympicTf() throws Exception {
		  
		  ModelAndView mv = new ModelAndView();
		  List<HashMap<String, Object>> topten = chartService.getTopTen();
			
		  mv.setViewName("tf");
		  mv.addObject("topten", topten);
		  
		  return mv;
	  }
	  
}
