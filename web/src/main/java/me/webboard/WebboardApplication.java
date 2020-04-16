package me.webboard;

import javax.sql.DataSource;

import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.SqlSessionFactoryBean;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.boot.web.servlet.support.SpringBootServletInitializer;
import org.springframework.context.annotation.Bean;
import org.springframework.core.io.Resource;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;
import org.springframework.web.filter.HiddenHttpMethodFilter;

@SpringBootApplication
@MapperScan(value= {"me.webboard.mapper"})
public class WebboardApplication extends SpringBootServletInitializer{

	public static void main(String[] args) {
		SpringApplication.run(WebboardApplication.class, args);
	}

	@Override protected SpringApplicationBuilder configure(SpringApplicationBuilder builder) { 
		return builder.sources(WebboardApplication.class); 
	}
	
	@Bean
	public SqlSessionFactory sqlSessionFactory(DataSource ds) throws Exception {
		SqlSessionFactoryBean ssfb = new SqlSessionFactoryBean();
		ssfb.setDataSource(ds);
		
		Resource[] res = new PathMatchingResourcePatternResolver().getResources("classpath:mappers/*Mapper.xml");
		
		ssfb.setMapperLocations(res);
		return ssfb.getObject();
	}
	@Bean
	public HiddenHttpMethodFilter hiddenHttpMethodFilter() {
		HiddenHttpMethodFilter httpFilter = new HiddenHttpMethodFilter();
		return httpFilter;
	}
}