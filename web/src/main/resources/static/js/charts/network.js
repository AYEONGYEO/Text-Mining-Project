// AM chart - Force directed network
// id = network
function network(word, data) {
	am4core.ready(function() {

//		console.log("* network chart 가 가져온 keyword : ");
//		console.log(word);
//		console.log(data);
		
		var words = data
		
		// Themes begin
		am4core.useTheme(am4themes_animated);
		// Themes endtext

		var chart = am4core.create("network", am4plugins_forceDirected.ForceDirectedTree);

		var networkSeries = chart.series.push(new am4plugins_forceDirected.ForceDirectedSeries())
		networkSeries.dataFields.linkWith = "linkWith";
		networkSeries.dataFields.name = "name";
		networkSeries.dataFields.id = "name";
		networkSeries.dataFields.value = "value";
		networkSeries.dataFields.children = "children";

		networkSeries.nodes.template.label.text = "{name}"
		networkSeries.fontSize = 20;
		networkSeries.linkWithStrength = 0;

		networkSeries.minRadius = 50;
		networkSeries.maxRadius = 100;


		var nodeTemplate = networkSeries.nodes.template;
		nodeTemplate.tooltipText = "{name}";
		nodeTemplate.fillOpacity = 1;
		nodeTemplate.label.hideOversized = true;
		nodeTemplate.label.truncate = true;

		var linkTemplate = networkSeries.links.template;
		linkTemplate.strokeWidth = 1;
		var linkHoverState = linkTemplate.states.create("hover");
		linkHoverState.properties.strokeOpacity = 1;
		linkHoverState.properties.strokeWidth = 2;

		nodeTemplate.events.on("over", function (event) {
		    var dataItem = event.target.dataItem;
		    dataItem.childLinks.each(function (link) {
		        link.isHover = true;
		    })
		})

		nodeTemplate.events.on("out", function (event) {
		    var dataItem = event.target.dataItem;
		    dataItem.childLinks.each(function (link) {
		        link.isHover = false;
		    })
		})
		
		networkSeries.data = [  
			{
				  "name": word,
				  "children" : words
				 
				}
		];
		}); // end am4core.ready()

	
}
