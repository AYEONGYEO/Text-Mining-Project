package me.webboard.service;

import java.util.HashMap;
import java.util.List;

import javax.servlet.http.HttpServletRequest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import me.webboard.dao.ChartDao;
import me.webboard.model.ChartVO;

@Service("ChartService")
public class ChartServiceImpl implements ChartService {

	@Autowired
	private ChartDao chartDao;
	
	@Override
	public List<ChartVO> getWordJson() {
		return chartDao.selectWordJson();
	}
	
	@Override
	public List<HashMap<String, Object>> getTopTen() {
		return chartDao.getTopTen();
	}
	
	@Override
	public List<HashMap<String, Object>> searchRealtedWord(String param) {
		return chartDao.searchRealtedWord(param);
	}
	
	@Override
	public List<HashMap<String, Object>> getBarChartValues(String name) {
		return chartDao.getBarChartValues(name);
	}
	
	@Override
	public List<HashMap<String, Object>> getArticleLinks(String name) {
		return chartDao.getArticleLinks(name);
	}
}
