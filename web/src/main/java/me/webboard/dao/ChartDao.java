package me.webboard.dao;

import java.util.HashMap;
import java.util.List;

import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import me.webboard.model.ChartVO;

@Repository("chDao")
public class ChartDao {

	@Autowired
	private SqlSessionTemplate sqlSession;
	
	public List<ChartVO> selectWordJson() {
		return sqlSession.selectList("chart.selectWordJson");
	}
	
	public List<HashMap<String, Object>> getTopTen() {
		return sqlSession.selectList("chart.getTopTen");
	}
	
	public List<HashMap<String, Object>> searchRealtedWord(String param) {
		return sqlSession.selectList("chart.searchRealtedWord", param);
	}
	
	public List<HashMap<String, Object>> getBarChartValues(String name) {
		return sqlSession.selectList("chart.getBarChartValues", name);
	}
	
	public List<HashMap<String, Object>> getArticleLinks(String name) {
		return sqlSession.selectList("chart.getArticleLinks", name);
	}
}
