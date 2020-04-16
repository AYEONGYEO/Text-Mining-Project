package me.webboard.service;

import java.util.HashMap;
import java.util.List;

import javax.servlet.http.HttpServletRequest;

import me.webboard.model.ChartVO;

public interface ChartService {

	List<ChartVO> getWordJson();
	
	List<HashMap<String, Object>> getTopTen();
	
	List<HashMap<String, Object>> searchRealtedWord(String param);
	
	List<HashMap<String, Object>> getBarChartValues(String name);
	
	List<HashMap<String, Object>> getArticleLinks(String name);
}
