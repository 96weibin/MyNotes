Hello everyone I'm weibin

Next, I will demo the UC of Create Porperties panel for blenders on the flowsheet

I created some blend materials in model data/material page, and specify some components and set the default, min, max value.

then go to flowsheet I have created some unit like this.

there are four tanks one blender unit, and T002, T003 and product stream of Attower connected to the blender BL-001

then we can click the blender unit to open the properties panel.

there is an Incomplete icon at the upper right corner, the tooltip is 'Please specify blend material'

below is basic info card. we can modify the name BL-001 to BL-002
modify the description Blender 001, and change the unit color.

below are two tabs configuration and balance

here are five cards In Configuration tab. blends、 recipe、 scheduling envlopes predecessors

in the first card we can set the default event color and default rate and default rate uom 

note that the default rate uom is Mbbl/Day

the default reate UOM come from General setting, go to general settings page and modify the blender default event UOM to Mbbl/hour

then back to flowsheet add a new blender unit

we can see the new blender BL001 default UOM changed to Mbbl/hour

In blends card the search box we can see all the blend material
we can select and search like input 001, select it and click the add icon

then the blend material created to the blends grid. and as the defualt blend.

and in the Recipe grid auto selected.

there are three colmn of blends grid.  default blends and description

then we can see the incomplete reason changed to please specify default rate.

we can set a default rate then because the default rate has been set. so the incomplete reason change to 'Please specify recipe components source'

There are two dropdown and one add icon and a recipe grid In recipe card.

User can selet basis as quantity or percent,
the recipe grid has 5 columns, source, material , min, max, default
the components of the selected blend material, displayed under the material column as the recipe components and other 4columns are mepty.

There's a problem here. The min, max, defaullt defined in the material are not 
brought here as the default min, max , default. the backend hasn't been resolved

click on empty source cell to open the dropdown, the dropdown list all the tanks, and rundown streams.rundown and connected tank is suggestion

map all source as tank.

then the incomplete reason changed to 'please specify rundwon in recipe'

then modify source map all rundownstreams then the blender is completed.

the rundown stream row cannot be deleted, and the default cell is disabled.

then we can add new blende material 002 to the blend grid.


then the incomplete reason changed to please specify rundown in recipe.

we can select the dropdown change blend to 002 recipe component

user auso can select the default blends to switch the recipe.

because no component is set in the material,  there is no row here.

we can click add icon to add a new row.

map rundown and material then the blender changed to complete.

and the envelopes and predacassors card and balance tab is same as mixer.

click the inspector icon. then the property panel is disabled

balance tab display the feeds, products, paramaters grids.

that is all 





