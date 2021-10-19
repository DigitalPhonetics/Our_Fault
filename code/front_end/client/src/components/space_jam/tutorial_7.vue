<template>
    <fragment>
        <div id = "wrapper">
            <br><br>
            <h2>Non-Interactive Board Elements</h2><br>

            <h4>Slider</h4> 
            The slider will change position as you complete modules and may be important for solving some modules.
            From top to bottom, the positions are: <b>Green, Yellow, Amber, Orange, Red</b><br><br>

            <h4>Shield Level Indicator</h4>
            The shield level indicator lets you know what <b>percentage</b> of your shield remains. If this reaches 0, you lose.<br><br>

            <h4>Shiled Time Remaining</h4>
            Let's you know how much time you have left in the game. If this reaches 0, you lose.<br><br>

            <h4>Warp Drive Indicator</h4>
            Lets you know what percentage of the warp drive engine you have filled. Once you reach 100%, you have won the game.<br><br>

             <svg
             id = "dial_exmaple"
             viewBox="0 0 1366 400">
                <g
                    id="g15" transform="translate(-25,-40)">
                    <rect
                    x="29"
                    y="45"
                    width="600"
                    height="350"
                    id="ship_console_background" />
                </g>
                <!-- Slider -->
                <g id="mini_wrapper" transform="translate(-650, 0)">
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

                    <text
                        id="warp_drive_power_text"
                        class="st11 st13 st21"
                        x="1023.0945"
                        y="303.7338">Warp Drive Power: {{warp_level}}%</text>  
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

                    <text
                        transform="matrix(1 0 0 1 1018 335.8027)"
                        class="st11 st13 st15"
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
                </g>
             </svg>
            <br>
        <div id = "navigation_buttons">
            <div id = "next_button">
                <b-button
                    variant="success"
                    @click="next_page">
                    Next
                </b-button>             </div>
            <div id = "back_button">
                <b-button
                    variant="danger"
                    @click="previous_page">
                    Back
                </b-button>             </div>
        </div>
        </div>


    </fragment>
</template>

<style scoped>

#next_button {
    float: right;
}

#back_button{
    float: left;
}

#wrapper{
    width: 80%;
    margin: auto;
}

</style>

<script>
export default {
    name: 'Tutorial_7',
    data(){ return {
        slider_position: "translate(-25, -200)",
        warp_level: 0,
        shield_level: 99,
        interval: 24,
        minute: 7,
        second: 59,
        percent: 99,
        }
    }, 
    methods:{
        next_page(){
            this.$router.push({
                name: 'Space_Jam',
            });
            this.$router.go()
        },
        previous_page(){
            this.$parent.tutorial_page -= 1;
        }        
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