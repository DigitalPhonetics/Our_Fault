<template>
    <fragment>
        <div id = "wrapper">
            <br><br>
            <h2>Button SequenceModule</h2><br>

            <h3>Features of the Button Sequence Module</h3>
            <ul>
                <li>Enabled buttons come in the following colors (shown below): <b>Green, Blue, </b>and <b>Amber</b></li>
                <li>You can tell if a button is actived if the fill color matches the border; inactive buttons have a gray fill color</li>
                <li>In the case that your spaceship has any disabled buttons, those will be shown in all grey</li>
                <li>In the case of mistakes, the button sequence will be reset to its original configuration</li>
            </ul><br>

            <h3>Try it out:</h3>
            <b>In this example your partner has just told you to activate the first amber button in the sequence</b>
            <br><br>
            <svg
             id = "dial_exmaple"
             viewBox="0 0 1366 200">

                <g
                id="g15" transform="translate(-25,-40)">
                <rect
                x="29"
                y="45"
                width="300"
                height="150"
                id="ship_console_background" />
                </g>                

                <!-- button_sequence -->
                <g id="button_sequence" transform="translate(-25,-231)">
                    <path @click="toggleButton"
                    id="button_sequence_0"
                    d="M 83.6,312.5 C 75,312.5 68,305.5 68,296.9 v -0.7 c 0,-8.6 7,-15.6 15.6,-15.6 8.6,0 15.6,7 15.6,15.6 v 0.7 c 0.1,8.6 -6.9,15.6 -15.6,15.6 z"
                    v-bind:class="[button_sequence_0_selected ? 'st26' : 'st2']" />

                    <path @click="toggleButton"
                    id="button_sequence_1"
                    d="m 131.6,312.5 c -8.6,0 -15.6,-7 -15.6,-15.6 v -0.7 c 0,-8.6 7,-15.6 15.6,-15.6 8.6,0 15.6,7 15.6,15.6 v 0.7 c 0.1,8.6 -6.9,15.6 -15.6,15.6 z"
                    v-bind:class="[button_sequence_1_selected ? 'st3' : 'st0']" />
                    
                    <g
                    id="button_sequence_2">
                    <path @click="toggleButton"
                        id="button_sequence_2"
                        d="m 179.6,312.5 c -8.6,0 -15.6,-7 -15.6,-15.6 v -0.7 c 0,-8.6 7,-15.6 15.6,-15.6 8.6,0 15.6,7 15.6,15.6 v 0.7 c 0.1,8.6 -6.9,15.6 -15.6,15.6 z"
                        v-bind:class="[button_sequence_2_selected ? 'st26': 'st2']" />
                    </g>

                    <g
                    transform="translate(-366.11434,11)"
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
            </svg>
            
        <div id = "navigation_buttons">
            <div id = "next_button" v-show="button_sequence_complete">
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
    name: 'Tutorial_4',
    data(){ return {
        // button_sequence
        button_sequence_0_selected: false,
        button_sequence_1_selected: false,
        button_sequence_2_selected: false,
        button_sequence_3_selected: false,
        button_sequence_4_selected: false,
        button_sequence_complete: false,
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
        reset_button(button){
            setTimeout(() => this[button] = false, 200)

        },
        toggleButton(event){
            event.preventDefault();
            if (this.game_state == "active") {
                var audio = new Audio(require('./sounds/button_sound.wav'));
                audio.play();

                this[event.target.id + '_selected'] = !this[event.target.id + '_selected'];
                if (event.target.id == "button_sequence_3") {
                    this.button_sequence_complete = true;
                    var complete_sound = new Audio(require('./sounds/module_complete.wav'));
                    complete_sound.play(); 
                }
                else{
                    var error_sound = new Audio(require('./sounds/buzzer.wav'));
                    error_sound.play();                     
                    this.reset_button(event.target.id + "_selected")
                }

            }    
        },               
    }    
}

</script>