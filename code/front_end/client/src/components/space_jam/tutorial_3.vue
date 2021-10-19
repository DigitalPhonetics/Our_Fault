<template>
    <fragment>
        <div id = "wrapper">
            <br><br>
            <h2>Dial Module</h2><br>

            <h3>Features of the Dials Module</h3>
            <ul>
                <li>Dials are made up of a pointer and multiple panels. Each panel is labeled with a number.</li>
                <li>If there are multiple dials on the control panel these are all part of the same module and all
                    dials need to be correctly positioned to complete the module.
                </li>
                <li>In the case of errors, the dial pointer(s) will be reset back to their original position.</li>
            </ul><br>

            <h3>Try it out:</h3>
            <b>In this example there is only one dial and your partner has just told you to set it to the largest even number</b>
            <br><br>
            <svg
             id = "dial_exmaple"
             viewBox="0 0 1366 300">

                <g
                id="g15" transform="translate(-25,-40)">
                <rect
                x="29"
                y="45"
                width="300"
                height="300"
                id="ship_console_background" />
                </g>                

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
                transform="matrix(1 0 0 1 65 222.7304)"
                class="st13 st24"
                id="dial_0_0_text">13</text>

                <text @click="rotateDialPointer"
                transform="matrix(1 0 0 1 101.2817 172.428)"
                class="st13 st24"
                id="dial_0_1_text">26</text>

                <text @click="rotateDialPointer"
                transform="matrix(1 0 0 1 165 155.4928)"
                class="st13 st24"
                id="dial_0_2_text">5</text>

                <text @click="rotateDialPointer"
                transform="matrix(1 0 0 1 215 172.428)"
                class="st13 st24"
                id="dial_0_3_text">30</text>

                <text @click="rotateDialPointer"
                transform="matrix(1 0 0 1 244.8707 220.8363)"
                class="st13 st24"
                id="dial_0_4_text">89</text>



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
            </svg>
            <br><br><br><br>
        <div id = "navigation_buttons">
            <div id = "next_button" v-show="dial_complete">
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
    name: 'Tutorial_3',
    data(){ return {
        dial_complete: false,
        dial_0_position: "rotate(-34, 174, 240)",
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
        reset_dial(){
            setTimeout(() => this.dial_0_position="rotate(-34, 174, 240)", 200)
        },
        rotateDialPointer(event){
            event.preventDefault()
            if (this.game_state == 'active') {
                this.dial_complete = false;
                var audio = new Audio(require('./sounds/dial_sound.wav'));
                audio.play();        
                if (event.target.id.includes("dial_0_0")) {
                    this.dial_0_position="rotate(-34, 176, 240)";
                }
                if (event.target.id.includes("dial_0_1")) {
                    this.dial_0_position="rotate(0, 176, 240)";
                }
                if (event.target.id.includes("dial_0_2")) {
                    this.dial_0_position="rotate(34, 176, 240)";
                }
                if (event.target.id.includes("dial_0_3")) {
                    this.dial_0_position="rotate(68, 176, 240)";
                    this.dial_complete = true;
                    var complete_sound = new Audio(require('./sounds/module_complete.wav'));
                    complete_sound.play();             
                }
                else {
                    var error_sound = new Audio(require('./sounds/buzzer.wav'));
                    error_sound.play();                    
                    this.reset_dial()
                }
                if (event.target.id.includes("dial_0_4")) {
                    this.dial_0_position="rotate(102, 176, 240)";
                }
            }
        },                
    }    
}

</script>