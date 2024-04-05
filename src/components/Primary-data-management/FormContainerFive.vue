<template>
  <div class="form-container-5 mb-96">
    <div class="bottom-layer">
      <div class="steps">
        <span class="bg-gradient-to-r from-blue-100 to-blue-100 p-3.5 py-2 rounded-xl">6</span> of <span id="total-steps">12</span>
      </div>
      <div class="move-icons">
        <i class="fa-solid fa-circle-chevron-left" id="left" @click="handleLeftClick"></i>
        <i
          id="right"
          class="fa-solid fa-circle-chevron-left"
          @click="handleRightClick"
        ></i>
      </div>
    </div>
    <div class="flex flex-col w-full gap-5 rounded-3xl drop-shadow-md backdrop-blur box-border p-7 bg-gradient-to-r from-blue-100 to-blue-100 container white">
        <div class="font-semibold"><h3>Coverage</h3></div>
        <div class="row-1">
            <div class="up mr-60"><p>Upper Left</p></div>
            <div class="content-upper-left">
                <div class="x-1">
                    <label for="x-ul">X</label>
                    <input type="text" class="w-44 h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" v-model="xUl" @input="validateNumberInput(xUl)">
                    <i
                    class="fa-solid fa-circle-check"
                    id="tick-left"
                    v-if="CorrectXUl && xUl"
                    ></i>
                    <i
                    id="cross-left"
                    class="fa-solid fa-circle-xmark"
                    v-if="!CorrectXUl && xUl"
                    ></i>
                </div>
                <div class="y-1">
                    <label for="y-ul">Y</label>
                    <input type="text" class="w-44 h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" id="y-ul" v-model="yUl" @input="validateNumberInput(yUl)">
                    <i
                    class="fa-solid fa-circle-check"
                    id="tick-left"
                    v-if="CorrectYUl && yUl"
                    ></i>
                    <i
                    id="cross-left"
                    class="fa-solid fa-circle-xmark"
                    v-if="!CorrectYUl && yUl"
                    ></i>
                </div>
            </div>
        </div>
        <div class="row-2">
            <div class="ur mr-60"><p>Upper Right</p></div>
            <div class="content-upper-right">
                <div class="x-2">
                    <label for="x-ur">X</label>
                    <input type="text" class="w-44 h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" v-model="xUr" @input="validateNumberInput(xUr)">
                    <i
                    class="fa-solid fa-circle-check"
                    id="tick-left"
                    v-if="CorrectXUr && xUr"
                    ></i>
                    <i
                    id="cross-left"
                    class="fa-solid fa-circle-xmark"
                    v-if="!CorrectXUr && xUr"
                    ></i>
                </div>
                <div class="y-2">
                    <label for="y-ur">Y</label> 
                    <input type="text" class="w-44 h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" v-model="yUr" @input="validateNumberInput(yUr)">
                    <i
                    class="fa-solid fa-circle-check"
                    id="tick-left"
                    v-if="CorrectYUr && yUr"
                    ></i>
                    <i
                    id="cross-left"
                    class="fa-solid fa-circle-xmark"
                    v-if="!CorrectYUr && yUr"
                    ></i>
                </div>
            </div>
        </div>
        <div class="row-3">
            <div class="lr mr-60"><p>Lower Right</p></div>
            <div class="content-lower-right">
                <div class="x-3">
                    <label for="x-lr">X</label>
                    <input type="text" class="w-44 h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" v-model="xLr" @input="validateNumberInput(xLr)">
                    <i
                    class="fa-solid fa-circle-check"
                    id="tick-left"
                    v-if="CorrectXlr && xLr"
                    ></i>
                    <i
                    id="cross-left"
                    class="fa-solid fa-circle-xmark"
                    v-if="!CorrectXlr && xLr"
                    ></i>
                </div>
                <div class="y-3">
                    <label for="y-lr">Y</label>
                    <input type="text" class="w-44 h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" v-model="yLr" @input="validateNumberInput(yLr)">
                    <i
                    class="fa-solid fa-circle-check"
                    id="tick-left"
                    v-if="CorrectYlr && yLr"
                    ></i>
                    <i
                    id="cross-left"
                    class="fa-solid fa-circle-xmark"
                    v-if="!CorrectYlr && yLr"
                    ></i>
                </div>
            </div>
        </div>
        <div class="row-4">
            <div class="ll mr-60"><p>Lower Left</p></div>
            <div class="content-lower-left">
                <div class="x-4">
                    <label for="x-ll">X</label>
                    <input type="text" class="w-44 h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" v-model="xLl" @input="validateNumberInput(xLl)">
                    <i
                    class="fa-solid fa-circle-check"
                    id="tick-left"
                    v-if="CorrectXLl && xLl"
                    ></i>
                    <i
                    id="cross-left"
                    class="fa-solid fa-circle-xmark"
                    v-if="!CorrectXLl && xLl"
                    ></i>
                </div>
                <div class="y-4">
                    <label for="y-l">Y</label>
                    <input type="text" class="w-44 h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" v-model="yLl" @input="validateNumberInput(yUl)">
                    <i
                    class="fa-solid fa-circle-check"
                    id="tick-left"
                    v-if="CorrectYLl && yLl"
                    ></i>
                    <i
                    id="cross-left"
                    class="fa-solid fa-circle-xmark"
                    v-if="!CorrectYLl && yLl"
                    ></i>
                </div>
            </div>
        </div>
    </div>
    
  </div>
</template>

<script>
import { ref,watch } from "vue";
import useValidate from "@vuelidate/core";
export default {
  setup(prop, { emit }) {
    const yLl = ref("");
    const CorrectYLl = ref(false);
    const xLl = ref("");
    const CorrectXLl = ref(false);
    const yLr = ref("");
    const CorrectYlr = ref(false);
    const xLr = ref("");
    const CorrectXlr = ref(false);
    const xUl = ref("");
    const CorrectXUl = ref(false);
    const yUl = ref("");
    const CorrectYUl = ref(false);
    const xUr = ref("");
    const CorrectXUr = ref(false);
    const yUr = ref("");
    const CorrectYUr = ref(false);
    const v$ = useValidate();

    const validateNumberInput = (input) => {
      return /^-?\d*\.?\d*$/.test(input);
    };
    
    // Watcher for xUl
    watch(xUl, (newValue, oldValue) => {
      if (validateNumberInput(newValue)) {
        CorrectXUl.value = true;
      } else {
        CorrectXUl.value = false;
      }
    });

    // Watcher for yUl
    watch(yUl, (newValue, oldValue) => {
      if (validateNumberInput(newValue)) {
        CorrectYUl.value = true;
      } else {
        CorrectYUl.value = false;
      }
    });

    // Watcher for xUr
    watch(xUr, (newValue, oldValue) => {
      if (validateNumberInput(newValue)) {
        CorrectXUr.value = true;
      } else {
        CorrectXUr.value = false;
      }
    });

    // Watcher for yUr
    watch(yUr, (newValue, oldValue) => {
      if (validateNumberInput(newValue)) {
        CorrectYUr.value = true;
      } else {
        CorrectYUr.value = false;
      }
    });

    // Watcher for xLr
    watch(xLr, (newValue, oldValue) => {
      if (validateNumberInput(newValue)) {
        CorrectXlr.value = true;
      } else {
        CorrectXlr.value = false;
      }
    });

    // Watcher for yLr
    watch(yLr, (newValue, oldValue) => {
      if (validateNumberInput(newValue)) {
        CorrectYlr.value = true;
      } else {
        CorrectYlr.value = false;
      }
    });

    // Watcher for xLl
    watch(xLl, (newValue, oldValue) => {
      if (validateNumberInput(newValue)) {
        CorrectXLl.value = true;
      } else {
        CorrectXLl.value = false;
      }
    });

    // Watcher for yLl
    watch(yLl, (newValue, oldValue) => {
      if (validateNumberInput(newValue)) {
        CorrectYLl.value = true;
      } else {
        CorrectYLl.value = false;
      }
    });

    const handleRightClick = () => {
      // const { emit } = getCurrentInstance(); // Access emit function using getCurrentInstance
      // Emit an event to the parent component to validate and proceed
      // Ensure that the necessary data is filled
      
        // Emit an event to the parent component
        // This event is caught in the parent component to proceed to the next step
        const data = {
        yLl: yLl.value,
        CorrectYLl: CorrectYLl.value,
        xLl: xLl.value,
        CorrectXLl: CorrectXLl.value,
        yLr: yLr.value,
        CorrectYlr: CorrectYlr.value,
        xLr: xLr.value,
        CorrectXlr: CorrectXlr.value,
        xUl: xUl.value,
        CorrectXUl: CorrectXUl.value,
        yUl: yUl.value,
        CorrectYUl: CorrectYUl.value,
        xUr: xUr.value,
        CorrectXUr: CorrectXUr.value,
        yUr: yUr.value,
        CorrectYUr: CorrectYUr.value
      };

       emit("update-data", data);

        console.log("emiting");
        emit("validate-and-proceed-form-five");
        
    };

    const handleLeftClick = () =>{
      emit("MoveBackToFour");
    }

    return {
      v$,
      yLl,
      CorrectYLl,
      xLl,
      CorrectXLl,
      yLr,
      CorrectYlr,
      xLr,
      CorrectXlr,
      xUl,
      CorrectXUl,
      yUl,
      CorrectYUl,
      xUr,
      CorrectXUr,
      yUr,
      CorrectYUr,
      handleRightClick,
      validateNumberInput,
      handleLeftClick,
    };
  },
};
</script>


<style scoped>
    body{
        padding: 0;
        margin: 0;
    }
    .form-container-5{
        display: flex;
        flex-direction: column;
       
    }

    .bottom-layer {
  width: 100%;
  padding: 1rem;
  text-align: center;
  font-size: 1.5rem;
 
  display: flex;
  gap: 0.4em;
  justify-content: center;
}

#right {
  transform: rotate(180deg);
  position: relative;
  left: 0.3em;
}



    
    

    .content-upper-left, .content-lower-left ,.content-lower-right, .content-upper-right{
        display: flex;
        justify-content: space-between;
        gap: 1em;
    }

    .x-4,.y-4,.x-3,.y-3, .x-2,.y-2, .x-1, .y-1{
        position: relative;
    }

    #tick-left{
        color: green;
        position: absolute;
        right: 1rem;
        top: 0.8rem;
    }

    #cross-left{
         color: red;
        position: absolute;
        right: 1rem;
        top: 0.8rem;
    }

    /* Base styles */

/* Styles for small phones (portrait and landscape) */
@media screen and (max-width: 640px) {
  /* Small mobile devices */
  .form-container-5{
    margin-left: 7.5rem;
  }
  .white{
    width: 100%;
  }
  .ll,.lr,.ur,.up{
    margin: 0;
  }
  label{
    margin-right: 0.3rem;
  }
  .content-upper-left{
    flex-direction: column;
  }
  .content-lower-right{
    flex-direction: column;
  }
  .content-upper-right{
    flex-direction: column;
  }
  .content-lower-left{
    flex-direction: column;
  }
 

}

@media screen and (min-width: 641px) and (max-width: 767px) {
  /* Big mobile devices */
 
}

@media screen and (min-width: 768px) and (max-width: 1023px) {
  /* Small laptops and tablets */
 
}

@media screen and (min-width: 1024px) and (max-width: 1279px) {
  /* Big laptops and desktops */
  
}
@media screen and (min-width: 1280px) and (max-width: 1440px) {
  /* Big laptops and desktops */

}
@media screen and (min-width: 1441px) {
  /* Big laptops and desktops */

}

    
</style>