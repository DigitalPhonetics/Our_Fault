<template>
    <fragment>
        <div id = "wrapper">
            <br><br>
            <h2>Switches Module</h2><br>

            <h3>Features of the Switches Module</h3>
            <ul>
                <li>The switches module is made of four switches, each switch has a left and right side </li>
                <li>You can tell which side of the switch (if any) is activated based on the fill color of the switch; gray filled switches are inactive</li>
                <li>Switches come in the following colors (shown below): <b>Green, Blue, </b>and <b>Amber</b></li>
                <li>When describing a switch's location, switches are numbered from the top down, i.e. the top switch is the first switch</li>
                <li>In the case of mistakes, you will be imediately notified and the switch sequence will be reset to its original configuration</li>
            </ul><br>

            <h3>Try it out:</h3>
            <b>In this example your partner has told you to:
                <ul>
                    <li>Activate the left side of the first switch </li>
                    <li>Activate the right side of the second</li>
                    <li>Activate the left side of the third</li>
                    <li>Activate the right side of the last switch</li>
                </ul></b>
            <br><br>
            <svg
             id = "dial_exmaple"
             viewBox="0 0 1366 400">

                <g
                id="g15" transform="translate(-25,-40)">
                <rect
                x="29"
                y="45"
                width="300"
                height="350"
                id="ship_console_background" />
                </g>                

                <!-- Toggle Swtiches -->

                <g id="toggle_0" transform="translate(-275,-20)">
                    <path @click="toggleSwitch"
                    v-bind:class="[right_toggle_0_selected ? 'st3' : 'st0']"
                    d="M472.2,115.1h-38.5v35h38.5c9.6,0,17.5-7.9,17.5-17.5l0,0C489.7,123,481.8,115.1,472.2,115.1z"
                    id="right_toggle_0" />

                    <path @click="toggleSwitch"
                    v-bind:class="[left_toggle_0_selected ? 'st3' : 'st0']"
                    d="M387.2,115.1c-9.6,0-17.5,7.9-17.5,17.5l0,0c0,9.6,7.9,17.5,17.5,17.5h38.5v-35H387.2z"
                    id="left_toggle_0"/>
                </g>

                <g id="toggle_1" transform="translate(-275,-20)">
                    <path @click="toggleSwitch"
                    v-bind:class="[right_toggle_1_selected ? 'st26' : 'st2']"
                    d="M472.2,171.1h-38.5v35h38.5c9.6,0,17.5-7.9,17.5-17.5l0,0C489.7,179,481.8,171.1,472.2,171.1z"
                    id="right_toggle_1" />

                    <path @click="toggleSwitch"
                    v-bind:class="[left_toggle_1_selected ? 'st26' : 'st2']"
                    d="M387.2,171.1c-9.6,0-17.5,7.9-17.5,17.5l0,0c0,9.6,7.9,17.5,17.5,17.5h38.5v-35H387.2z"
                    id="left_toggle_1" />
                </g>

                <g id="toggle_2" transform="translate(-275,-20)">
                    <path @click="toggleSwitch"
                    v-bind:class="[right_toggle_2_selected ? 'st27' : 'st1']"
                    d="M472.2,230h-38.5v35h38.5c9.6,0,17.5-7.9,17.5-17.5l0,0C489.7,237.9,481.8,230,472.2,230z"
                    id="right_toggle_2" />

                    <path @click="toggleSwitch"
                    v-bind:class="[left_toggle_2_selected ? 'st27' : 'st1']"
                    d="M387.2,230c-9.6,0-17.5,7.9-17.5,17.5l0,0c0,9.6,7.9,17.5,17.5,17.5h38.5v-35H387.2z"
                    id="left_toggle_2" />
                </g>

                <g id="toggle_3" transform="translate(-275,-20)">
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
                transform="matrix(1.1853574,0,0,1,-350,-20)">
                <path
                v-bind:class="[toggle_complete ? 'st11' : 'st5']"
                d="M 489.5,76.9 H 368.4 c -1.9,0 -3.5,-3.6 -3.5,-8.1 v 0 c 0,-4.4 1.6,-8.1 3.5,-8.1 h 121.1 c 1.9,0 3.5,3.6 3.5,8.1 v 0 c 0,4.4 -1.6,8.1 -3.5,8.1 z"
                id="toggle_indicator" />
                <text v-show="toggle_complete"
                    transform="matrix(1 0 0 1 366 74.4341)"
                    class="st22 st13 st21"
                    id="toggle_indicator_text">Module Complete </text>
                </g>
            </svg>
            
        <div id = "navigation_buttons">
            <div id = "next_button" v-show="toggle_complete">
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
    name: 'Tutorial_5',
    data(){ return {
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
        game_state: "active",
        }
    },
    methods:{
        next_page(){
            this.$parent.tutorial_page += 1;
        },
        previous_page(){
            this.$parent.tutorial_page -= 1;
        },
        reset_toggles(){
            setTimeout(() => this._reset(), 200)

        },
        _reset(){
            this.right_toggle_0_selected = false;
            this.left_toggle_0_selected = false;   
            this.right_toggle_1_selected = false;
            this.left_toggle_1_selected = false;   
            this.right_toggle_2_selected = false;
            this.left_toggle_2_selected = false;
            this.right_toggle_3_selected = false;
            this.left_toggle_3_selected = false;
            this.toggle_complete = false            
        },
        toggleSwitch(event){
            event.preventDefault();
            if (this.game_state == 'active') {
                this[event.target.id + '_selected'] = !this[event.target.id + '_selected'];
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
                if (this.left_toggle_0_selected && this.right_toggle_1_selected && this.left_toggle_2_selected && this.right_toggle_3_selected){
                    this.toggle_complete = true;
                    var complete_sound = new Audio(require('./sounds/module_complete.wav'));
                    complete_sound.play();                     
                }
                if (this.right_toggle_0_selected || this.left_toggle_1_selected || this.right_toggle_2_selected || this.left_toggle_3_selected){
                    var error_sound = new Audio(require('./sounds/buzzer.wav'));
                    error_sound.play();                     
                    this.reset_toggles()
                }
            }
        },               
    }    
}

</script>