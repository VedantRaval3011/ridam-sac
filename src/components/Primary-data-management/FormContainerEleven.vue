<template>
  <div class="form-container-eleven mb-32">
    <div class="bottom-layer">
      <div class="steps">
        <span class=" bg-gradient-to-r from-blue-100 to-blue-100 p-3.5 py-2 rounded-xl">12</span> of <span id="total-steps">12</span>
      </div>
      <div class="move-icons">
        <i class="fa-solid fa-circle-chevron-left" @click="handleLeftClick"></i>
        <i
          id="right"
          class="fa-solid fa-circle-chevron-left"
          @click="handleRightClick"
        ></i>
      </div>
    </div>
    <div class="flex flex-col gap-5 text-center rounded-3xl drop-shadow-md backdrop-blur box-border p-7 bg-gradient-to-r from-blue-100 to-blue-100 container white">
      <div class="font-semibold">
        <h3>Data Quality</h3>
      </div>
      <div class="process-desc">
        <label for="pd" class="">Process Description </label><br />
        <input type="text" class="w-full h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" v-model="pd" @input="ValidatePd" />
        <i
          class="fa-solid fa-circle-check"
          id="tick"
          v-if="Correctpd && pd"
        ></i>
        <i
          id="cross"
          class="fa-solid fa-circle-xmark"
          v-if="!Correctpd && pd"
        ></i>
      </div>
      <div class="report">
        <label for="accReport" class="accR">Source contribution attribute accuracy report</label> <br />
        <input type="text" class="w-full h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" v-model="accReport" @input="ValidateAccR" /><i
          class="fa-solid fa-circle-check"
          id="tick"
          v-if="CorrectAccR && accReport"
        ></i>
        <i
          id="tick"
          class="fa-solid fa-circle-check"
          v-if="!CorrectAccR && accReport"
        ></i>
      </div>

    

      <div class="horpor">
        <label for="horpor" class="heading-horpor">Horizontal positional report accuracy</label><br />
        <input
          type="text"
          class="w-full h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border"
          v-model="horpor"
          @input="ValidateHorpor"
        /><i
          class="fa-solid fa-circle-check"
          id="tick"
          v-if="Correcthorpor && horpor"
        ></i>
        <i
          id="cross"
          class="fa-solid fa-circle-xmark"
          v-if="!Correcthorpor && horpor"
        ></i>
      </div>
    </div>
    
     <div class="flex gap-3 mt-6">
      <input type="checkbox" class="p-6 w-5 h-5 mt-1"  v-model="confirmation" @change="handleConfirmationChange">
      <label for="confirmation-checkbox" class="">Data you have entered is best of your knowledge</label>
    </div>
    
  </div>
</template>

<script>
import { ref, watch } from "vue";
import useValidate from "@vuelidate/core";

export default {
  setup(props, { emit }) {
  const pd = ref("");
  const Correctpd = ref(false);
   const accReport = ref("");
  const CorrectAccR = ref(true);
    const v$ = useValidate();
  const horpor = ref("");
  const Correcthorpor = ref(false);
   const confirmation = ref(false);
 

  const ValidatePd = () => {
    Correctpd.value =  pd.value.length > 3;
  };

  watch(pd, () => {
    ValidatePd();
  });

   const ValidateAccR = () => {
    CorrectAccR.value = accReport.value.length > 3 ;
    console.log(CorrectAccR.value);
  };

  watch(accReport, () => {
    ValidateAccR();
  });

  


  const ValidateHorpor = () => {
    Correcthorpor.value = horpor.value.length > 3;
  };

  watch(horpor, () => {
    ValidateHorpor();
  });


  const handleConfirmationChange = () => {
      if (confirmation.value) {
         const data = {
            pd: pd.value,
            Correctpd: Correctpd.value,
            accReport: accReport.value,
            CorrectAccR: CorrectAccR.value,
            horpor: horpor.value,
            Correcthorpor: Correcthorpor.value
        }
      emit("update-data", data);
      } else {
        alert("Please confirm that the data you have entered is the best of your knowledge.");
      }
    };

  

  const handleRightClick = () => {

   
    emit('validate-and-proceed-form-eleven');   
  };

  const handleLeftClick = () =>{
    console.log('emittt');
    emit('MoveBackToTen');
  }

  return {
    ValidatePd,
    pd,
    confirmation,
    Correctpd,
    ValidateAccR,
    accReport,
    handleConfirmationChange,
    horpor,
    Correcthorpor,
    handleLeftClick,
    v$,
    handleRightClick,
  };
}


}


  

    

</script>

<style scoped>
body {
  padding: 0;
  margin: 0;
}

.white{
  width: 100%;
}

.bottom-layer {
  width: 100%;
  padding: 1rem;
  text-align: center;
  font-size: 1.5em;
  display: flex;
  gap: 0.3em;
  margin-left: 6rem;
}

#right {
  transform: rotate(180deg);
  position: relative;
  left: 0.2em;
}

.horpor,.report,.process-desc{
  position: relative;
}

#tick-1{
  color: green;
  position: absolute;
  right: 0.3em;
}
i{
  cursor: pointer;
}

#current-step {
  background: linear-gradient(
    to bottom,
    #b2e2f1,
    #b2e2f1,
    #b2e2f1,
    #b2e2f1,
    #b2e2f1
  ); /* Gradient fill */
  padding: 15px 20px 12px 20px;
  border: none;
  border-radius: 16px;
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2);
}

.row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
}

#tick {
  color: green;
  position: absolute;
  top: 2.15em;
  right: 1em;
}

#cross {
  color: crimson;
  position: absolute;
   top: 2.15em;
  right: 1em;
}





.heading {
  position: relative;
  right: 200px;
}





#confirmation-checkbox{
  padding: 0;
  margin: 0;
  width: 23px;
  height: 23px;
}

.confirmation-checkbox{
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 179px;
  margin-left: 85px;
}

.confirmation-checkbox label{
  margin-top: 15px;
}

@media screen and (max-width: 640px) {
  /* Small mobile devices */
  .white{
    width: 100%;
    
  }
  .form-container-eleven{
    position: relative;
    right: 31%;
    font-size: 0.80rem;
  }

  .bottom-layer{
    margin-left: 5em;
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
