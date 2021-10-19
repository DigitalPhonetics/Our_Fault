<style
   type="text/css"
   id="style314">
	.st0{fill:#848484;stroke:#00DBFF;stroke-width:3;stroke-miterlimit:10;}
	.st1{fill:#848484;stroke:#F4A61C;stroke-width:3;stroke-miterlimit:10;}
	.st2{fill:#848484;stroke:#7BDD0A;stroke-width:3;stroke-miterlimit:10;}
	.st3{fill:#00DBFF;stroke:#00DBFF;stroke-width:3;stroke-miterlimit:10;}
	.st4{fill:#7BDD0A;}
	.st5{fill:#848484;}
	.st6{fill:#00DBFF;}
	.st7{fill:#F4A61C;}
	.st8{fill:#F4DC00;}
	.st9{fill:#FF6700;}
	.st10{fill:#EF0000;}
	.st11{fill:#FFFFFF;}
	.st12{enable-background:new    ;}
	.st13{font-family:'CourierNew', monospace;}
	.st14{font-size:18.6724px;}
	.st15{font-size:41.4779px;}
	.st16{fill:#4C4C4C;}
	.st17{fill:#282828;}
	.st18{font-size:28.4026px;}
	.st19{font-family:'Verdana';}
	.st20{font-size:50px;}
	.st21{font-size:14px;}
	.st22{fill:#0081C1;}
	.st23{fill:#AEF0FF;}
	.st24{font-size:30px;}
	.st25{fill:#C6C6C6;}
	.st26{fill:#7BDD0A;stroke:#7BDD0A;stroke-width:3;stroke-miterlimit:10;}
	.st27{fill:#F4A61C;stroke:#F4A61C;stroke-width:3;stroke-miterlimit:10;}
  .st28{font-size:43.4779px;}

	.footer
    {
        position: absolute;
        bottom:30px;
        left:0px;
        right:0px;
        height:50px;
        margin-bottom:0px;
        display: flex;
    }
  .messagebox
    {
        padding: 35px;
        height: calc(100vh - 100px);
        overflow-y: auto;
    }
</style>

<template>
<div id="test_app">
  <svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   version="1.1"
   id="Layer_1"
   x="0px"
   y="0px"
   viewBox="0 0 1366 450"
   xml:space="preserve"
   sodipodi:docname="Spaceship Board_Final.svg"
   inkscape:version="0.92.5 (2060ec1f9f, 2020-04-08)"><sodipodi:namedview
   pagecolor="#ffffff"
   bordercolor="#666666"
   borderopacity="1"
   objecttolerance="10"
   gridtolerance="10"
   guidetolerance="10"
 />

    <!-- Background -->
    <g
      id="g15" transform="translate(-25,-40)">
      <rect
      x="29"
      y="45"
      width="1216"
      height="350"
      id="ship_console_background" />
    </g>

    <!-- Start Button (temporary) -->
    <g @click="startGame" id="start_buttpn_and_text"   transform="translate(-25,-40)">
    <rect
    class="st26"
    x="29"
    y="410"
    width="100"
    height="40"
    id="start_button"/>
    <text
    transform="matrix(1 0 0 1 35 439)"
    class="st11 st13 st18"
    id="start_button_text">Start</text>
    </g>

    <!-- Toggle Swtiches -->

    <g id="toggle_0" transform="translate(-25,-20)">
      <path @click="toggleSwitch"
      v-bind:class="[right_toggle_0_selected ? 'st3' : 'st0']"
      d="M472.2,115.1h-38.5v35h38.5c9.6,0,17.5-7.9,17.5-17.5l0,0C489.7,123,481.8,115.1,472.2,115.1z"
      id="right_toggle_0" />

      <path @click="toggleSwitch"
      v-bind:class="[left_toggle_0_selected ? 'st3' : 'st0']"
      d="M387.2,115.1c-9.6,0-17.5,7.9-17.5,17.5l0,0c0,9.6,7.9,17.5,17.5,17.5h38.5v-35H387.2z"
      id="left_toggle_0"/>
    </g>

    <g id="toggle_1" transform="translate(-25,-20)">
      <path @click="toggleSwitch"
      v-bind:class="[right_toggle_1_selected ? 'st26' : 'st2']"
      d="M472.2,171.1h-38.5v35h38.5c9.6,0,17.5-7.9,17.5-17.5l0,0C489.7,179,481.8,171.1,472.2,171.1z"
      id="right_toggle_1" />

      <path @click="toggleSwitch"
      v-bind:class="[left_toggle_1_selected ? 'st26' : 'st2']"
      d="M387.2,171.1c-9.6,0-17.5,7.9-17.5,17.5l0,0c0,9.6,7.9,17.5,17.5,17.5h38.5v-35H387.2z"
      id="left_toggle_1" />
    </g>

    <g id="toggle_2" transform="translate(-25,-20)">
      <path @click="toggleSwitch"
      v-bind:class="[right_toggle_2_selected ? 'st27' : 'st1']"
      d="M472.2,230h-38.5v35h38.5c9.6,0,17.5-7.9,17.5-17.5l0,0C489.7,237.9,481.8,230,472.2,230z"
      id="right_toggle_2" />

      <path @click="toggleSwitch"
      v-bind:class="[left_toggle_2_selected ? 'st27' : 'st1']"
      d="M387.2,230c-9.6,0-17.5,7.9-17.5,17.5l0,0c0,9.6,7.9,17.5,17.5,17.5h38.5v-35H387.2z"
      id="left_toggle_2" />
    </g>

    <g id="toggle_3" transform="translate(-25,-20)">
      <path @click="toggleSwitch"
      v-bind:class="[right_toggle_3_selected ? 'st3' : 'st0']"
      d="M472.2,286h-38.5v35h38.5c9.6,0,17.5-7.9,17.5-17.5l0,0C489.7,293.9,481.8,286,472.2,286z"
      id="right_toggle_3" />

      <path @click="toggleSwitch"
      v-bind:class="[left_toggle_3_selected ? 'st3' : 'st0']"
      d="M387.2,286c-9.6,0-17.5,7.9-17.5,17.5l0,0c0,9.6,7.9,17.5,17.5,17.5h38.5v-35H387.2z"
      id="left_toggle_3" />
    </g>

    <!-- Toggle Indicator -->
    <g
      id="toggle_complete_indicator"
      transform="matrix(1.1853574,0,0,1,-103.497101,-20)">
      <path
      v-bind:class="[toggle_complete ? 'st11' : 'st5']"
      d="M 489.5,76.9 H 368.4 c -1.9,0 -3.5,-3.6 -3.5,-8.1 v 0 c 0,-4.4 1.6,-8.1 3.5,-8.1 h 121.1 c 1.9,0 3.5,3.6 3.5,8.1 v 0 c 0,4.4 -1.6,8.1 -3.5,8.1 z"
      id="toggle_indicator" />
      <text v-show="toggle_complete"
        transform="matrix(1 0 0 1 366 74.4341)"
        class="st22 st13 st21"
        id="toggle_indicator_text">Module Complete </text>
    </g>


    <!-- Button Array -->

    <g id="memory_column_0" transform="translate(-18,-20)">
      
      <path @click="toggleButton"
      v-bind:class="[memory_0_0_selected ? 'st27' : 'st1']"
      d="M534,146.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C541,162.1,534,155.1,534,146.5z"
      id="memory_0_0" />

      <path @click="toggleButton"
      v-bind:class="[memory_0_1_selected ? 'st27' : 'st1']"
      d="M534,191.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C541,207.1,534,200.1,534,191.5z"
      id="memory_0_1" />
 
      <path @click="toggleButton"
      v-bind:class="[memory_0_2_selected ? 'st26' : 'st2']"
      d="M534,239.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C541,255.1,534,248.1,534,239.5z"
      id="memory_0_2" />

      <path @click="toggleButton"
      v-bind:class="[memory_0_3_selected ? 'st3' : 'st0']"
      d="M534,287.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C541,303.1,534,296.1,534,287.5z"
      id="memory_0_3" />
    </g>    

    <g id="memory_column_1" transform="translate(-18,-20)">

      <path @click="toggleButton"
      v-bind:class="[memory_1_0_selected ? 'st26' : 'st2']"
      d="M578,146.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C585,162.1,578,155.1,578,146.5z"
      id="memory_1_0" />

      <path @click="toggleButton"
      v-bind:class="[memory_1_1_selected ? 'st3' : 'st0']"
      d="M578,191.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C585,207.1,578,200.1,578,191.5z"
      id="memory_1_1" />

      <path @click="toggleButton"
      v-bind:class="[memory_1_2_selected ? 'st26' : 'st2']"
      d="M578,239.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C585,255.1,578,248.1,578,239.5z"
      id="memory_1_2" />

      <path @click="toggleButton"
      v-bind:class="[memory_1_3_selected ? 'st27' : 'st1']"
      d="M578,287.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C585,303.1,578,296.1,578,287.5z"
      id="memory_1_3" />
    </g>

    <g id="memory_column_2" transform="translate(-18,-20)">
      <path @click="toggleButton"
      v-bind:class="[memory_2_0_selected ? 'st27' : 'st1']"
      d="M621,146.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C628,162.1,621,155.1,621,146.5z"
      id="memory_2_0" />

      <path @click="toggleButton"
      v-bind:class="[memory_2_1_selected ? 'st26' : 'st2']"
      d="M621,191.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C628,207.1,621,200.1,621,191.5z"
      id="memory_2_1" />

      <path @click="toggleButton"
      v-bind:class="[memory_2_2_selected ? 'st3' : 'st0']"
      d="M621,239.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C628,255.1,621,248.1,621,239.5z"
      id="memory_2_2" />

      <path @click="toggleButton"
      v-bind:class="[memory_2_3_selected ? 'st3' : 'st0']"
      d="M621,287.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C628,303.1,621,296.1,621,287.5z"
      id="memory_2_3" />
    </g> 

    <!-- Button Array Indicator -->
    <g
      id="memory_indicator_group"
      transform="matrix(1.0798142,0,0,1,-68.528288,-20)">
      <path
      v-bind:class="[memory_complete ? 'st11' : 'st5']"
      d="M 658.7,76.9 H 537.5 c -1.9,0 -3.5,-3.6 -3.5,-8.1 v 0 c 0,-4.4 1.6,-8.1 3.5,-8.1 h 121.1 c 1.9,0 3.5,3.6 3.5,8.1 v 0 c 0.1,4.4 -1.5,8.1 -3.4,8.1 z"
      id="memory_indicator" />
    <text v-show="memory_complete"
      transform="matrix(1 0 0 1 535 74.4341)"
      class="st22 st13 st21"
      id="memory_indicator_text">Module Complete</text>
    </g>

    <!-- Slider -->

    <g id="slider_bar" transform="translate(-25,-42)">
      <rect
      x="725.7"
      y="69"
      class="st4"
      width="39"
      height="99.7"
      id="slider_level_green" />

      <rect
      x="725.7"
      y="172.7"
      class="st8"
      width="39"
      height="82.4"
      id="slider_level_yellow" />

      <rect
      x="725.7"
      y="259.2"
      class="st7"
      width="39"
      height="55.6"
      id="slider_level_amber" />

      <rect
      x="725.7"
      y="318.9"
      class="st9"
      width="39"
      height="37.1"
      id="slider_level_orange" />

      <rect
      x="725.7"
      y="360"
      class="st10"
      width="39"
      height="22"
      id="slider_level_red" />
    </g>

<!-- Different slider indicator positions -->
    <g
      :transform=slider_position
      id="slider_level_indicator">
      <polygon
      class="st11"
      points="707.7,269.2 749.6,287 707.7,304.8  "
      id="slider" />
      <path
      d="M709.7,272.2l34.8,14.8l-34.8,14.8V272.2 M705.7,266.2v41.6l49-20.8L705.7,266.2L705.7,266.2z"
      id="slider_outline" />
    </g> 
  
  <!-- Dial 0 -->

  <g
    id="dial_0_and_pointer" transform="translate(-25,-20)">

    <!--panels  -->
    <g id="dial_body">
      <path @click="rotateDialPointer"
      class="st23"
      d="M104.4,233.1c0.3-4.8,1.1-9.5,2.5-14.3c1.9-6.6,4.6-12.7,8.1-18.2l-38.9-28.3c-6.7,10-12,21.3-15.4,33.5     c-2.6,9.1-4,18.3-4.4,27.4L104.4,233.1z"
      id="dial_0_0" />

      <path @click="rotateDialPointer"
      class="st23"
      d="M120.8,192.5c7.4-8.8,16.9-15.6,27.4-19.9l-14.8-45.7c-20.1,7.5-37.9,20.3-51.5,37.3L120.8,192.5z"
      id="dial_0_1" />

      <path @click="rotateDialPointer"
      class="st23"
      d="M157.8,169.5c10.8-2.7,22.3-2.8,33.7,0l15-45.7c-21.6-6-43.5-5.7-63.6,0L157.8,169.5z"
      id="dial_0_2" />

      <path @click="rotateDialPointer"
      class="st6"
      d="M216.1,126.9l-15,45.7c11,4.4,20.4,11.4,27.6,20l38.9-28.3C254.5,147.8,237,134.6,216.1,126.9z"
      id="dial_0_3" />

      <path @click="rotateDialPointer"
      class="st6"
      d="M234.6,200.7c6,9.6,9.6,20.6,10.5,32.1l48.1-0.1c-1-21.7-7.9-42.6-19.7-60.3L234.6,200.7z"
      id="dial_0_4" />
    </g>

    <!-- Panel labels -->
    <text @click="rotateDialPointer"
    transform="matrix(1 0 0 1 73.5455 222.7304)"
    class="st13 st24"
    id="dial_0_0_text">1</text>

    <text @click="rotateDialPointer"
    transform="matrix(1 0 0 1 101.2817 172.428)"
    class="st13 st24"
    id="dial_0_1_text">15</text>

    <text @click="rotateDialPointer"
    transform="matrix(1 0 0 1 157.5271 155.4928)"
    class="st13 st24"
    id="dial_0_2_text">27</text>

    <text @click="rotateDialPointer"
    transform="matrix(1 0 0 1 220.1038 172.428)"
    class="st13 st24"
    id="dial_0_3_text">3</text>

    <text @click="rotateDialPointer"
    transform="matrix(1 0 0 1 244.8707 220.8363)"
    class="st13 st24"
    id="dial_0_4_text">18</text>



    <!-- pointer -->
    <g
      id="dial_0_pointer"
      :transform=dial_0_position>
        <path
      class="st11"
      d="M186.2,260.7c-9.7,4.3-21.2,1.4-27.8-6.9c-4.4-5.6-6.1-12.8-4.5-19.7l0.1-0.6l-27.3-62.3l51.5,44.6l0.6,0.1    c6.5,0.6,12.3,3.7,16.3,8.8c8.1,10.1,6.4,24.9-3.8,33C189.8,258.8,188.1,259.8,186.2,260.7L186.2,260.7z"
      id="dial_0_pointer_fill" />
        <path
      d="M132.1,178.4l44.4,38.4l1,0.9l1.3,0.1c5.9,0.5,11.2,3.4,14.9,8c7.4,9.3,5.8,22.8-3.4,30.2c-1.5,1.2-3.1,2.1-4.8,2.9    c-8.9,3.9-19.4,1.3-25.5-6.3c-4.1-5.1-5.6-11.7-4.2-18.1l0.3-1.3l-0.5-1.2L132.1,178.4 M121.3,163.8l30.6,69.8    c-1.6,7.3-0.1,15.2,4.9,21.4c7.4,9.3,19.9,12,30.2,7.5c2-0.9,3.9-2,5.6-3.4c11-8.8,12.8-24.8,4.1-35.8c-4.5-5.7-11-8.9-17.7-9.5    L121.3,163.8L121.3,163.8z"
      id="dial_0_pointer_outline" />
    </g>


    <!-- Dial 0 Indicator -->
    <g
      id="dial_0_complete_indicator">
      <path
      v-bind:class="[dial_complete ? 'st11' : 'st5']"
      d="M280.6,76.9H75.7c-4.4,0-8.1-3.6-8.1-8.1l0,0c0-4.4,3.6-8.1,8.1-8.1h204.9c4.4,0,8.1,3.6,8.1,8.1l0,0   C288.7,73.2,285.1,76.9,280.6,76.9z"
      id="dial_0_indicator" />
    <text v-show="dial_complete"
      transform="matrix(1 0 0 1 111.2749 74.4341)"
      class="st22 st13 st21"
      id="dial_0_indicator_text">Module Complete</text>
    </g>
  </g>


<!-- Dial 1 -->

<g id="dial_1_and_pointer" transform="translate(-25,-20)">

<!-- Panels -->
  <g id="dial_1">
		<path @click="rotateDialPointer"
      class="st23"
      d="M1035.3,232.7c0.3-4.8,1.2-9.5,2.5-14.3c1.9-6.6,4.6-12.7,8.1-18.2l-38.9-28.3c-6.7,10-12,21.3-15.4,33.5     c-2.6,9.1-4,18.3-4.4,27.4L1035.3,232.7z"
      id="dial_1_0" />

  	<path @click="rotateDialPointer"
      class="st23"
      d="M1051.8,192.1c7.4-8.8,16.9-15.6,27.4-19.9l-14.8-45.7c-20.1,7.5-37.9,20.3-51.5,37.3L1051.8,192.1z"
      id="dial_1_1" />

		<path @click="rotateDialPointer"
      class="st23"
      d="M1088.8,169.1c10.8-2.7,22.3-2.8,33.7,0l15-45.7c-21.6-6-43.5-5.7-63.6,0L1088.8,169.1z"
      id="dial_1_2" />

		<path @click="rotateDialPointer"
      class="st6"
      d="M1147,126.5l-15,45.7c11,4.4,20.4,11.4,27.6,20l38.9-28.3C1185.5,147.4,1167.9,134.3,1147,126.5z"
      id="dial_1_3" />

		<path @click="rotateDialPointer"
      class="st6"
      d="M1165.5,200.3c6,9.6,9.7,20.6,10.5,32.1l48.1-0.1c-0.9-21.7-7.9-42.6-19.7-60.3L1165.5,200.3z"
      id="dial_1_4" />
	</g>

<!-- Panel Lables-->
	<text @click="rotateDialPointer"
   transform="matrix(1 0 0 1 1004.5105 222.3488)"
   class="st13 st24"
   id="dial_1_0_text">2</text>

	<text @click="rotateDialPointer"
   transform="matrix(1 0 0 1 1032.2467 172.0464)"
   class="st13 st24"
   id="dial_1_1_text">13</text>

	<text @click="rotateDialPointer"
   transform="matrix(1 0 0 1 1088.4921 155.1111)"
   class="st13 st24"
   id="dial_1_2_text">32</text>

	<text @click="rotateDialPointer"
   transform="matrix(1 0 0 1 1144.0688 171.0464)"
   class="st13 st24"
   id="dial_1_3_text">25</text>

	<text @click="rotateDialPointer"
   transform="matrix(1 0 0 1 1175.8357 220.4547)"
   class="st13 st24"
   id="dial_1_4_text">19</text>


  <!-- Pointer -->
    <g
    id="dial_1_pointer"
    :transform=dial_1_position>    
      <path
    class="st11"
    d="M1090.2,256.4c-7.4-7.6-8.8-19.3-3.3-28.5c3.7-6.1,9.8-10.2,16.9-11.2l0.7-0.1l48.7-47.4l-23.7,63.9l0.2,0.6    c1.7,6.3,0.8,12.8-2.5,18.3c-6.7,11.1-21.1,14.7-32.2,8.1C1093.2,259.1,1091.6,257.8,1090.2,256.4L1090.2,256.4z"
    id="dial_1_pointer_fill" />
      <path
    d="M1148.2,176.8l-20.4,55l-0.5,1.2l0.3,1.2c1.6,5.7,0.8,11.7-2.3,16.8c-6.1,10.2-19.3,13.5-29.5,7.4c-1.6-1-3.1-2.1-4.4-3.4    c-6.8-7-8-17.7-3-26c3.3-5.6,9-9.3,15.5-10.2l1.3-0.2l0.9-0.9L1148.2,176.8 M1158.1,161.6l-54.6,53.1c-7.4,1-14.2,5.3-18.3,12.1    c-6.1,10.1-4.3,22.8,3.6,30.9c1.5,1.5,3.2,2.9,5.2,4.1c12.1,7.2,27.7,3.3,35-8.8c3.7-6.2,4.5-13.4,2.7-19.9L1158.1,161.6    L1158.1,161.6z"
    id="dial_1_pointer_outline" />
    </g>

  <!-- Dial 1 Indicator -->
  <g
    id="g448">
    <path
    v-bind:class="[dial_complete ? 'st11' : 'st5']"
    d="M1200.2,76.9H995.3c-4.4,0-8.1-3.6-8.1-8.1l0,0c0-4.4,3.6-8.1,8.1-8.1h204.9c4.4,0,8.1,3.6,8.1,8.1l0,0   C1208.3,73.2,1204.6,76.9,1200.2,76.9z"
    id="dial_1_indicator" />
    <text v-show="dial_complete"
    transform="matrix(1 0 0 1 1030.8499 74.4341)"
    class="st22 st13 st21"
    id="dial_1_indicator_text">Module Complete</text>
  </g>
</g>


  <!-- button_sequence -->
  <g id="button_sequence" transform="translate(-25,-20)">
    <path @click="toggleButton"
      id="button_sequence_0"
      d="M 83.6,312.5 C 75,312.5 68,305.5 68,296.9 v -0.7 c 0,-8.6 7,-15.6 15.6,-15.6 8.6,0 15.6,7 15.6,15.6 v 0.7 c 0.1,8.6 -6.9,15.6 -15.6,15.6 z"
      v-bind:class="[button_sequence_0_selected ? 'st27' : 'st1']" />

    <path @click="toggleButton"
      id="button_sequence_1"
      d="m 131.6,312.5 c -8.6,0 -15.6,-7 -15.6,-15.6 v -0.7 c 0,-8.6 7,-15.6 15.6,-15.6 8.6,0 15.6,7 15.6,15.6 v 0.7 c 0.1,8.6 -6.9,15.6 -15.6,15.6 z"
      v-bind:class="[button_sequence_1_selected ? 'st3' : 'st0']" />
    
    <g
      id="button_sequence_2">
      <path @click="toggleButton"
        id="path566"
        d="m 179.6,312.5 c -8.6,0 -15.6,-7 -15.6,-15.6 v -0.7 c 0,-8.6 7,-15.6 15.6,-15.6 8.6,0 15.6,7 15.6,15.6 v 0.7 c 0.1,8.6 -6.9,15.6 -15.6,15.6 z"
        class="st5" />
      <path
        id="path568"
        d="m 179.6,282 c 7.8,0 14.1,6.3 14.1,14.1 v 0.7 c 0,7.8 -6.3,14.1 -14.1,14.1 -7.8,0 -14.1,-6.3 -14.1,-14.1 v -0.7 c 0,-7.8 6.3,-14.1 14.1,-14.1 m 0,-3 c -9.4,0 -17.1,7.7 -17.1,17.1 v 0.7 c 0,9.4 7.7,17.1 17.1,17.1 9.4,0 17.1,-7.7 17.1,-17.1 v -0.7 c 0.1,-9.4 -7.6,-17.1 -17.1,-17.1 z"
        class="st5" />
    </g>

    <g
      transform="translate(-366.11434,11.079508)"
      id="g63-3">
      <path @click="toggleButton"
        v-bind:class="[button_sequence_3_selected ? 'st27' : 'st1']"
        d="m 578,287.5 c 0,-8.6 7,-15.6 15.6,-15.6 h 0.7 c 8.6,0 15.6,7 15.6,15.6 0,8.6 -7,15.6 -15.6,15.6 h -0.7 c -8.6,0 -15.6,-7 -15.6,-15.6 z"
        id="button_sequence_3" />
    </g>

    <path @click="toggleButton"
      id="button_sequence_4"
      d="m 275.6,314.5 c -8.6,0 -15.6,-7 -15.6,-15.6 v -0.7 c 0,-8.6 7,-15.6 15.6,-15.6 8.6,0 15.6,7 15.6,15.6 v 0.7 c 0.1,8.6 -6.9,15.6 -15.6,15.6 z"
        v-bind:class="[button_sequence_4_selected ? 'st3' : 'st0']"/>

    <!-- button_sequence Indicator -->
    <g
      id="g454">
      <path
      v-bind:class="[button_sequence_complete ? 'st11' : 'st5']"
      d="M 280.6,351.3 H 75.7 c -4.4,0 -8.1,-3.6 -8.1,-8.1 v 0 c 0,-4.4 3.6,-8.1 8.1,-8.1 h 204.9 c 4.4,0 8.1,3.6 8.1,8.1 v 0 c 0,4.5 -3.6,8.1 -8.1,8.1 z"
      id="button_sequence_indicator"/>
    </g>
    <text v-show="button_sequence_complete"
      class="st22 st13 st21"
      id="button_sequence_indicator_text"
      style="font-size:15px;font-family:CourierNew;fill:#0081c1"
      x="105.274902"
      y="349">Module Complete</text>        
  </g>

<!-- Shield Countdown Info -->
<text
   transform="matrix(1 0 0 1 792.6898 308.884)"
   class="st12"
   id="text403"><tspan
     x="0"
     y="0"
     class="st11 st13 st14"
     id="tspan399">Shield Time </tspan><tspan
     x="0"
     y="22.4"
     class="st11 st13 st14"
     id="tspan401">Remaining:</tspan></text>


  <!-- Countdown Timer -->

  <text v-show="!text_big"
    transform="matrix(1 0 0 1 1018 335.8027)"
    class="st11 st13 st15"
    id="text405">{{minute | formatTime}}:{{second | formatTime}}</text>
  <text v-show="text_big"
    transform="matrix(1 0 0 1 1018 335.8027)"
    class="st10 st13 st28"
    id="text405">{{minute | formatTime}}:{{second | formatTime}}</text>

  <!-- Shield Percent Box -->
  <g
    id="g105"
    transform="translate(-26, -40)">
    <g
    id="shield_indicator_box">
      <path
    class="st16"
    d="M826.7,302.7c-5.8,0-10.5-3.4-10.5-7.5V116c0-4.1,4.7-7.5,10.5-7.5h108c5.8,0,10.5,3.4,10.5,7.5v179.2    c0,4.1-4.7,7.5-10.5,7.5H826.7z"
    id="path407" />
      <path
    class="st17"
    d="M934.7,109.6c5,0,9,2.9,9,6.4v179.2c0,3.5-4,6.4-9,6.4h-108c-5,0-9-2.9-9-6.4V116c0-3.5,4-6.4,9-6.4H934.7     M934.7,107.5h-108c-6.6,0-12,3.9-12,8.6v179.2c0,4.7,5.4,8.6,12,8.6h108c6.6,0,12-3.9,12-8.6V116    C946.7,111.3,941.3,107.5,934.7,107.5L934.7,107.5z"
    id="path409" />
    </g>

    <text
    transform="matrix(1 0 0 1 828 155)"
    class="st11 st13 st18"
    id="text413">Shield</text>
    <text
    transform="matrix(1 0 0 1 837 189)"
    class="st11 st13 st18"
    id="text415">Level</text>

    <!-- Shield Percent Remaining -->
    <text
    transform="matrix(1 0 0 1 821 266)"
    class="st7 st19 st20"
    font-weight="bold"
    id="shield_level">{{shield_level}}%</text>
  </g> 

  <!-- Warp Drive Indicator -->
  <g
    id="g426"
    transform="translate(-25, -27)">
    <path
    id="path420"
    d="m 1010.8,315.5 c -8.6,0 -15.6,-7 -15.6,-15.6 v -0.7 c 0,-8.6 7,-15.6 15.6,-15.6 h 200.7 c 8.6,0 15.6,7 15.6,15.6 v 0.7 c 0,8.6 -7,15.6 -15.6,15.6 z"
    class="st5" />
    <g
    id="g424">
    <path
    id="path422"
    d="m 1211.5,285 c 7.8,0 14.1,6.3 14.1,14.1 v 0.7 c 0,7.8 -6.3,14.1 -14.1,14.1 h -200.7 c -7.8,0 -14.1,-6.3 -14.1,-14.1 v -0.7 c 0,-7.8 6.3,-14.1 14.1,-14.1 h 200.7 m 0,-3 h -200.7 c -9.4,0 -17.1,7.7 -17.1,17.1 v 0.7 c 0,9.4 7.7,17.1 17.1,17.1 h 200.7 c 9.4,0 17.1,-7.7 17.1,-17.1 v -0.7 c 0.1,-9.4 -7.6,-17.1 -17.1,-17.1 z"
    class="st6" />
      </g>
   <g v-show="warp_level > 1" id="warp_progress">
    <circle
      class="st3"
      id="path4141"
      cx="1010.875"
      cy="299"
      r="14.316" />
      <rect
      class="st3"
      id="rect4143"
      :width= 2.02*warp_level
      height="28.556896"
      x="1010.8"
      y="285.4028" />
      <circle v-show="warp_level == 100"
      class="st3"
      id="path4141-3"
      :cx=1010.875+2.02*warp_level
      cy="299"
      r="14.316" />  
   </g>

  <!-- <g
    id="g426-3"
    transform="translate(49.449652,-15.412076)" />
    <path
    id="warp_drive_progress"
    d="m 1009.1098,313.5 104.0076,0.90885 v -28.41002 l -104.0076,-0.90885 c -6.7845,-0.0593 -12.36812,6.41255 -12.36812,14.20501 v 0 c 0,7.79246 5.58332,14.20501 12.36812,14.20501 z"
    class="st3" /> -->

  <text
    id="warp_drive_power_text"
    class="st11 st13 st21"
    x="1023.0945"
    y="303.7338">Warp Drive Power: {{warp_level}}%</text>  
 </g>

<g
  v-show="game_result == 'victory'"
  id="victory_box">
  <rect
    class="st21"
    opacity="0.6"
    x="4"
    y="5"
    width="1216"
    height="350"
    id="ship_console_background" />
  <rect
    class="st2"
    x="204"
    y="100"
    width="800"
    height="150"/>
  <text
    style="font-size:50px;font-family:CourierNew;fill:#ffffff"
    x="230"
    y="190">
    CONGRATULATIONS! YOU WIN!
  </text>
  <a href="//https://hcm-lab.de/surveys/index.php/169427?lang=en">
    <text 
      x="380"
      y="230"
      style="font-size:20;font-family:CourierNew;fill:#ffffff" >
      Click Here go to the post game questionnaire
    </text>
  </a>
</g>

<g
  v-show="game_result == 'defeat'"
  id="victory_box">
  <rect
    class="st21"
    opacity="0.6"
    x="4"
    y="5"
    width="1216"
    height="350"
    id="ship_console_background" />
  <rect
    class="st1"
    x="204"
    y="100"
    width="800"
    height="150"/>
  <text
    style="font-size:42px;font-family:CourierNew;fill:#ffffff"
    x="230"
    y="190">
    DEFEAT! BETTER LUCK NEXT TIME.
  </text>
  <a href="//https://hcm-lab.de/surveys/index.php/169427?lang=en">
  <text   
    x="380"
    y="230"
    style="font-size:20;font-family:CourierNew;fill:#ffffff" >
    Click Here go to the post game questionnaire
  </text>
</a>
</g>

  </svg>
  
    <div v-if="has_token"  class="messagebox" ref="messagebox">
    <chatmessage
      v-for="(msg, index) in messages"
        :key="index"
        :party="msg.party"
        :message="msg.message"
    />
  </div>
  <div v-if="has_token" class="footer">
      <input 
        ref="usermsg"
        id="usermsg"
        placeholder="Enter your message here"
        v-model="userMessage"
        @keyup.enter="sendMessage"
        style="flex:1; display:block;"/>
      <b-button
        variant="primary"
        :disabled="!connected"
        @click="sendMessage"
      >
        Send
      </b-button>
  </div>

  <b-modal id="connectionalert" hide-footer>
    <template v-slot:modal-title>
      No valid connection to server
    </template>
    <div>
        Login expired (or connection problem) - please try to log in again!
    </div>
    <b-button @click="$router.replace('/')" block variant="danger">Login</b-button>
  </b-modal>    
</div>
</template>

<script>
import Chatmessage from '../chatmessage.vue';
import { mapState } from "vuex";

export default {
    name: 'Space_Jam',
    components: {
      chatmessage: Chatmessage,
    },
  computed: {
      
      ...mapState(["token"]),
    },
    created() {
      if(this.has_token()) {
        // only setup a connection if we get a token from server
        this.socket = new WebSocket("ws://127.0.0.1:44123/ws?token=" + this.token);
        this.socket.onopen = (event) => {
          //this.startDialog();
        };
        this.socket.onmessage = (msg) => {
          var content = JSON.parse(msg.data)
          if (content['topic'] == 'sys_utterance') {
            this.messages.shift();
            this.messages.push({party: 'system', message: content['msg']});            
          }
          if (content['topic'] == 'memory') {
            for (let col = 0; col < 3; col++) {
              for (let row = 0; row < 4; row++) {
                this['memory_' + String(col) + '_' + String(row) + "_selected"] = false;
              }
            }
            this[content['msg'] + '_selected'] = true;
          }
          if (content['topic'] == 'slider'){
            var slider_dict = {
              'green': "translate(-25,-200)",
              'red': "translate(-25, 44)",
              'orange': "translate(-25, 10)",
              'amber': "translate(-25, -40)",
              'yellow': "translate(-25, -110)"}
            this.slider_position = slider_dict[content['msg']]
          }
          if (content['topic'] == 'dial_0'){
            var dial_0_dict = {
              0: "rotate(-34, 176, 240)",
              1: "rotate(0, 176, 240)",
              2: "rotate(34, 176, 240)",
              3: "rotate(68, 176, 240)",
              4: "rotate(102, 176, 240)"
            }
            this.dial_0_position = dial_0_dict[content['msg']];
          }
          if (content['topic'] == 'dial_1'){
            var dial_1_dict = {
              0: "rotate(-102,1107,240)",
              1: "rotate(-68,1107,240)",
              2: "rotate(-34,1107,240)",
              3: "rotate(0,1107,240)",
              4: "rotate(34, 1107, 240)"
            }
            this.dial_1_position = dial_1_dict[content['msg']]
          }
          if (content['topic'] == 'toggles') {
            for (let i = 0; i < 4; i++) {
              this["right_toggle_" + String(i) + "_selected"] = false;
              this["left_toggle_" + String(i) + "_selected"] = false;
            }            
          }
          if (content['topic'] == 'button_sequence') {
            for (let i = 0; i < 5; i++) {
              this["button_sequence_" + String(i) + "_selected"] = false;
            }
          }
          if (content['topic'] == 'module_complete' && this.game_state == "active") {
            this[content['msg']] = true;
            // TODO: at some point make this not hard-coded
            var audio = new Audio(require('./sounds/module_complete.wav'));
            audio.play();            
          }
          // allows completed modules to be moved out of position
          if (content['topic'] == 'module_incomplete' && this.game_state == "active"){
            this[content['msg']] = false;
            console.log(content['msg'])
          }
          if (content['topic'] == 'time_penalty') {
            var audio = new Audio(require('./sounds/buzzer.wav'));
            audio.play();
            this.time_penalty = parseInt(content['msg'])
            this.flashText()
          }
        }
      }
      else {
        // don't connect - no token
      }
    },     
  data() { return {
    // toggle swtiches
    right_toggle_0_selected: false,
    left_toggle_0_selected: false,    
    right_toggle_1_selected: false,
    left_toggle_1_selected: false,    
    right_toggle_2_selected: false,
    left_toggle_2_selected: false,
    right_toggle_3_selected: false,
    left_toggle_3_selected: false,
    toggle_complete: false,
    // button array
    memory_0_0_selected: false,
    memory_0_1_selected: false,
    memory_0_2_selected: false,
    memory_0_3_selected: false,
    memory_1_0_selected: false,
    memory_1_1_selected: false,
    memory_1_2_selected: false,
    memory_1_3_selected: false,
    memory_2_0_selected: false,
    memory_2_1_selected: false,
    memory_2_2_selected: false,
    memory_2_3_selected: false,
    memory_complete: false,
    text_big: false,
    // dials
    dial_complete: false,
    dial_0_position: "rotate(-34, 174, 240)",
    dial_1_position: "rotate(-102,1107,240)",
    // button_sequence
    button_sequence_0_selected: false,
    button_sequence_1_selected: false,
    button_sequence_2_selected: false,
    button_sequence_3_selected: false,
    button_sequence_4_selected: false,
    button_sequence_complete: false,
    // slider
    // red: 44, orange: 10, amber: -40, yellow -110 
    slider_position: "translate(-25, -200)",
    warp_level: 0,
    shield_level: 99,
    minute: 9,
    second: 59,
    percent: 99,
    game_state: "inactive",
    messages: [],
    userMessage: '',
    connected: false,
    socket: null,
    domain: 0,
    game_result: null,
    time_penalty: 0
    }
  },
  methods: {

    has_token: function() {
        return (typeof this.token !== 'undefined') && (this.token != null) && (this.token.length > 0);
    },
    toggleButton(event){
      event.preventDefault();
      if (this.game_state == "active") {
        if (event.target.id.includes("memory")) {
          for (let col = 0; col < 3; col++) {
            for (let row = 0; row < 4; row++) {
              this['memory_' + String(col) + '_' + String(row) + "_selected"] = false;
            }
          }        
        }
        var audio = new Audio(require('./sounds/button_sound.wav'));
        audio.play();

        this[event.target.id + '_selected'] = !this[event.target.id + '_selected'];
        this.socket.send(JSON.stringify({
          access_token: this.token,
          topic: 'button_event',
          domain: this.domain,
          id: event.target.id,
          active: this[event.target.id + '_selected']
        }));  
      }    
    },

    toggleSwitch(event){
      event.preventDefault();
      if (this.game_state == 'active') {
        this[event.target.id + '_selected'] = !this[event.target.id + '_selected'];
        this.socket.send(JSON.stringify({
          access_token: this.token,
          topic: 'toggle_switch_event',
          domain: this.domain,
          id: event.target.id,
          active: this[event.target.id + '_selected']
        }));
        var audio = new Audio(require('./sounds/toggle_sound.wav'));
        audio.play();          
        if (this[event.target.id + '_selected']) {
          if (event.target.id.includes("left")) {
            this[event.target.id.replace("left", "right") + '_selected'] = false;
          }
          else {
            this[event.target.id.replace("right", "left") + '_selected'] = false;
          }
        }
      }
    },
    rotateDialPointer(event){
      event.preventDefault()
      if (this.game_state == 'active') {
        this.socket.send(JSON.stringify({
          access_token: this.token,
          topic: 'dial_event',
          domain: this.domain,
          id: event.target.id,
          // just get index of panel
          position: event.target.id.slice(7, 8)
        }));
        var audio = new Audio(require('./sounds/dial_sound.wav'));
        audio.play();        
        if (event.target.id.includes("dial_0_0")) {
          this.dial_0_position="rotate(-34, 176, 240)"
        }
        if (event.target.id.includes("dial_0_1")) {
          this.dial_0_position="rotate(0, 176, 240)"
        }
        if (event.target.id.includes("dial_0_2")) {
          this.dial_0_position="rotate(34, 176, 240)"
        }
        if (event.target.id.includes("dial_0_3")) {
          this.dial_0_position="rotate(68, 176, 240)"
        }
        if (event.target.id.includes("dial_0_4")) {
          this.dial_0_position="rotate(102, 176, 240)"
        }
        if (event.target.id.includes("dial_1_0")) {
          this.dial_1_position="rotate(-102,1107,240)"
        }
        if (event.target.id.includes("dial_1_1")) {
          this.dial_1_position="rotate(-68,1107,240)"
        }
        if (event.target.id.includes("dial_1_2")) {
          this.dial_1_position="rotate(-34,1107,240)"
        }
        if (event.target.id.includes("dial_1_3")) {
          this.dial_1_position="rotate(0,1107,240)"
        }
        if (event.target.id.includes("dial_1_4")) {
          this.dial_1_position="rotate(34, 1107, 240)"
        }
      }
    },

  startGame(event){
    event.preventDefault();
    if (this.has_token()){
      if (this.game_state == "inactive") {
        this.game_state="active";
        this._tick();
        this.interval = setInterval(this._tick, 1000);
        this.messages = [];
        this.socket.send(JSON.stringify({
            topic: "start_dialog",
            domain: this.domain,
            access_token: this.token,
          }
        ));
      }
    }
    else {
      this.$bvModal.show('connectionalert'); 
    } 
  },
  endGame(){
    if (this.game_state != "finished"){
      this.game_state = "finished"
      if (this.warp_level == 100) {
        this.game_result = "victory";
      }
      else {
        this.game_result = "defeat";
      }
      if (this.has_token()){
        this.socket.send(JSON.stringify({
          topic: "game_over",
          condition: this.game_result,
          access_token: this.token,
        }));
      }
      this.minute = 0;
      this.second = 0 ;     
    };
  },
  flashText(){
    this.text_big = true
    setTimeout(() => this.text_big = false, 500)
  },
  _tick: function(){
    // TODO: debug why this only works hard-coded
    this.warp_level = 0
    if (this.dial_complete){
      this.warp_level += 25;
    }
    if (this.toggle_complete){
      this.warp_level += 25;
    }
    if (this.button_sequence_complete) {
      this.warp_level += 25;
    }
    if (this.memory_complete) {
      this.warp_level += 25;
    }

    this.shield_level = Math.floor((this.minute *60 + this.second) / 6.0)

    //if second is 0 and minute is 0, clear the interval
    if (this.minute <= 0 && this.second <= this.time_penalty || this.warp_level == 100){
      this.endGame()
    }
    //if second is not 0, just decrement second
    if (this.second >= this.time_penalty + 1) {
      this.second--;
      this.second = this.second - this.time_penalty;
      this.time_penalty = 0;
      return;
    }
    //if second is 0 and minute is not 0, decrement minute and set second to 59
    if (this.minute !== 0 && this.second <= this.time_penalty) {
      this.minute--;
      this.second = 59;
      this.second = this.second - this.time_penalty;
      this.time_penalty = 0;
    }
  },
  sendMessage: function (event) {
    event.preventDefault();

    if (this.has_token()) {
      if (this.messages.length > 1){
        this.messages.shift()
      }
      this.messages.push({party: 'user', message: this.userMessage});
      this.socket.send(JSON.stringify({
        access_token: this.token,
        topic: 'user_utterance',
        domain: this.domain,
        msg: this.userMessage,
      }));
      this.userMessage = '';
    } else {
      this.$bvModal.show('connectionalert');
    } 
  },
  scrollToBottom: function () {
    var container = this.$refs.messagebox;
    container.scrollTop = container.scrollHeight;
  },  
  },
  filters: {
    formatTime: function(value) {
      if (value >= 10) {
        return value;
      }
      if (value < 0){
        return "00"
      }
      return "0" + value;
    }
  }
}
</script>