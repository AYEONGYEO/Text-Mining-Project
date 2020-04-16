//AM charts - word cloud 
// id = wordcloud

//index.html에서 thymeleaf inline 을 통해 controller 에서 전달한 json 값 가져오기
//console.log(words);

am4core.ready(function() {

// Themes begin
am4core.useTheme(am4themes_animated);
// Themes end


var chart = am4core.create("wordcloud", am4plugins_wordCloud.WordCloud);
var series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());

series.accuracy = 4;
series.step = 15;
series.rotationThreshold = 0.7;
series.maxCount = 10;
series.minWordLength = 2;
series.labels.template.margin(4,4,4,4);
series.maxFontSize = am4core.percent(50);

//series.text = "Though yet of Hamlet our dear brother's death T, love 한글 한글 사랑해 사랑해"; 

//console.log("test************");
//console.log(words);
//console.log(series.dataFields.word);

series.data = words;
series.dataFields.word = "noun";
series.dataFields.value = "count";


series.colors = new am4core.ColorSet();
series.colors.passOptions = {}; // makes it loop

//series.labelsContainer.rotation = 45;
series.angles = [0,-90];
series.fontWeight = "700"

setInterval(function () {
  series.dataItems.getIndex(Math.round(Math.random() * (series.dataItems.length - 1))).setValue("value", Math.round(Math.random() * 10));
 }, 10000)

}); // end am4core.ready()