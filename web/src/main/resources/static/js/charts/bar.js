// AM chart - Clustered Bar Chart
function barchart(data){
	am4core.ready(function() {

		// Themes begin
		am4core.useTheme(am4themes_animated);
		// Themes end

		 // Create chart instance
		var chart = am4core.create("barchart", am4charts.XYChart);
		
//		console.log(topten);
	
		var bar_value_array = [];
		var testarray = new Array();
		
		var testValue = data;
//		console.log(testValue);
		
		for (var i=0 ; i<topten.length ; i++) {
			var flag = 0;
			var compare_noun = topten[i].noun;
			
			for (var j=0 ; j<testValue.length ; j++) {
				var noun = testValue[j].noun;
				
				if(compare_noun == noun) {
					testarray.push(testValue[j].percentage);
					flag = 1;
					break;
				}
			}
			if (flag == 0) {
				testarray.push(0)
			}
			
		};
		
		for(var i=0 ; i<topten.length ; i++){
			
			var y  = topten[i].noun;
			var x1 = testarray[i].toFixed(2);
			var x2 = topten[i].percentage.toFixed(2);
			
			var tem = [{
				"words" : y, 
				"x1" : x1, 
				"x2" : x2 
				}];
			
			Array.prototype.push.apply(bar_value_array, tem);
			
		}
//		console.log(bar_value_array);


		chart.data = bar_value_array;

		// Create axes
		var categoryAxis = chart.yAxes.push(new am4charts.CategoryAxis());
		categoryAxis.dataFields.category = "words";
		categoryAxis.numberFormatter.numberFormat = "#";
		categoryAxis.renderer.inversed = true;
		categoryAxis.renderer.grid.template.location = 0;
		categoryAxis.renderer.cellStartLocation = 0.1;
		categoryAxis.renderer.cellEndLocation = 0.9;

		var  valueAxis = chart.xAxes.push(new am4charts.ValueAxis()); 
		valueAxis.renderer.opposite = true;

		// Create series
		function createSeries(field, name) {
		  var series = chart.series.push(new am4charts.ColumnSeries());
		  series.dataFields.valueX = field;
		  series.dataFields.categoryY = "words";
		  series.name = name;
		  series.columns.template.tooltipText = "{name}: [bold]{valueX}[/]";
		  series.columns.template.height = am4core.percent(100);
		  series.sequencedInterpolation = true;

		  var valueLabel = series.bullets.push(new am4charts.LabelBullet());
		  valueLabel.label.text = "{valueX}";
		  valueLabel.label.horizontalCenter = "left";
		  valueLabel.label.dx = 10;
		  valueLabel.label.hideOversized = false;
		  valueLabel.label.truncate = false;

		  var categoryLabel = series.bullets.push(new am4charts.LabelBullet());
		  categoryLabel.label.text = "{name}";
		  categoryLabel.label.horizontalCenter = "right";
		  categoryLabel.label.dx = -10;
		  categoryLabel.label.fill = am4core.color("#fff");
		  categoryLabel.label.hideOversized = false;
		  categoryLabel.label.truncate = false;
		}

		createSeries("x1", "selected date");
		createSeries("x2", "whole date");

		}); // end am4core.ready()
}
