package me.webboard.model;

public class RelatedVO {
	private int id;
	private String noun;
	private String rel;
	private int count;
	
	// getter, setter
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getNoun() {
		return noun;
	}
	public void setNoun(String noun) {
		this.noun = noun;
	}
	public String getRelatedword() {
		return rel;
	}
	public void setRelatedword(String rel) {
		this.rel = rel;
	}
	public int getCount() {
		return count;
	}
	public void setCount(int count) {
		this.count = count;
	}
	
	
	
}
