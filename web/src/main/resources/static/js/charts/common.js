window.onload = function() {
	var top = document.getElementsByClassName("topword");
	var date_btn = document.getElementsByClassName("date_btn");

	// top 10 list에서 key word 클릭 시
	for(var i=0 ; i < top.length ; i++){
		// 에고 네트워크 그래프 불러오기
		top[i].addEventListener("click", function(){
			requestNetworkChart(this.text);
		});
		
		// 기사 링크 불러오기
		top[i].addEventListener("click", function(){
			requestArticleLink(this.text);
		});
	};
	
	// 날짜 버튼 클릭시 , 바 차트에 데이터 가져오기
	for(var i=0 ; i < date_btn.length ; i++){
		date_btn[i].addEventListener("click", requestBarChart);
	};

}

function requestArticleLink(word) {
	
	console.log("** " + word + "에 대해 기사 링크를 검색")
	
	$.ajax({
		url : "articlelink",
		type : "POST",
		data : word,
		dataType : "json",
		contentType : "application/json; charset=utf-8",
		success :
			function(data){
				var links = data;
				var tbody = document.getElementById('link_table');
				
				if(tbody.rows.length==0){
				}
				else{
					$("#link_table").children().remove();
				}
				
				//링크 개수 20개 만큼 html에 table row 추가
				for(var i=0 ; i < links.length ; i++){
					
					var row = tbody.insertRow( tbody.rows.length ); // 하단에 추가
					var cell_id = row.insertCell(0);
					var cell_url = row.insertCell(1);
					var url_string = "<a style='margin-left:20px;' href='" + links[i].url + "'>" + links[i].url + "</a>"
					
					cell_id.innerHTML = i+1;
					cell_url.innerHTML = url_string;
				};
				
		},
		error :
			function(){
				console.log("error in search article link");
		},
		complete :
			function(){
				console.log("search article link ajax 실행");
		}
	})
}

function requestBarChart() {
//	var date = this.innerText;
//	date = date.replace(/-/gi, "");

	var date = this.value;

	table_name = "WORDTF_" + date + "_TB";
//	console.log(table_name);
	
	
	$.ajax({
		url : "barchart",
		type : "POST",
		data : table_name,
		dataType : "json",
		contentType : "application/json; charset=utf-8",
		success :
			function(data){
				barchart(data); 	//bar chart 실행
		},
		error :
			function(){
				console.log("error in barchart ajax");
		},
		complete :
			function(){
				console.log("barchart ajax 실행");
		}
	})
	
}

function requestNetworkChart(word) {
	
	console.log("클릭시 requestNetworkChart 실행, 클릭 한 단어 : " + word);
	
	$.ajax({
		url : "requestNetworkChart",
		type : "POST",
		data : word,
		dataType : "json",
		contentType : "application/json; charset=utf-8;",
		success : function(data) {
			network(word, data);	//에고 네트워크 그래프 실행
		},
		error : function() {
			console.log("network chart request fail");
		},
		complete : function() {
			console.log("request network chart ajax 실행 ");
		}
		
	});
}



//function ego(){
////	alert("ego")
////	var word = this.text;	//type = string, 값 잘 가져옴
//	console.log("ego function start");
//	
//	$("#network").removeClass("invisible");
//	$("#network").addClass("visible");
//	
//	var word = "연기";
//	param = {
//			"param": word
//	};
//	
//	$.ajax({
//		url : "ego",
//		type : "GET",
//		data : param,
//		dataType : "json",
//		contentType : "application/json; charset=utf-8;",
//		success : function(data) {
//			network(word, data);	//에고 네트워크 그래프 실행
//		},
//		error : function() {
//			console.log("network chart request fail");
//		},
//		complete : function() {
//			console.log("ajax 실행 완료");
//		}
//	});
//	
//}

