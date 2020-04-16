package me.webboard.model;

public class TopwordNgramVO {

	private int id;
	private String topword;
	private String relatedword;
	private int count;
	
	//getter and setter
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getTopword() {
		return topword;
	}
	public void setTopword(String topword) {
		this.topword = topword;
	}
	public String getRelatedword() {
		return relatedword;
	}
	public void setRelatedword(String relatedword) {
		this.relatedword = relatedword;
	}
	public int getCount() {
		return count;
	}
	public void setCount(int count) {
		this.count = count;
	}
	
}
