<template>
  <div class="form-container-three mb-96">
    <div class="bottom-layer">
    <div class="steps">
      <span class="bg-gradient-to-r from-blue-100 to-blue-100 p-3.5 py-2 rounded-xl">4</span> of <span id="total-steps">12</span>
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
      <div class=" "><h3>Contact Information</h3></div>
      <div class="row-one">
        <div class="contact-person">
          <label for="contact-person">Contact Person</label><br />
          <div class="contact-person-input">
            <input type="text" id="contact-person" class="bg-blue-50 shadow-md border-none text-base" v-model="ContactPerson" @input="ValidateContactPerson"/>
            <i
              class="fa-solid fa-circle-check"
              id="tick-left"
              v-if="CorrectContactPerson && ContactPerson"
            ></i>
            <i
              id="cross-left"
              class="fa-solid fa-circle-xmark"
              v-if="!CorrectContactPerson && ContactPerson"
            ></i>
          </div>
        </div>
        <div class="organization">
          <label for="organization">Organization</label><br />
          <div class="organization-input">
            <input type="text" id="organization" class="bg-blue-50 shadow-md border-none text-base pr-8" v-model="organization" @input="ValidateOrganization" />
            <i
              class="fa-solid fa-circle-check"
              id="tick-right"
              v-if="CorrectOrganization && organization"
            ></i>
            <i
              id="cross-right"
              class="fa-solid fa-circle-xmark"
              v-if="!CorrectOrganization && organization"
            ></i>
          </div>
        </div>
      </div>
      <div class="row-two">
        <div class="mailing-address">
          <label for="mailing-address">Mailing Address</label><br />
          <div class="mailing-address-input">
            <input type="text" id="mailing-address" class="bg-blue-50 shadow-md border-none text-base pr-8" v-model="MailAddress" @input="ValidateMailAddress"/>
            <i
              class="fa-solid fa-circle-check"
              id="tick-left"
              v-if="CorrectMailAddress && MailAddress"
            ></i>
            <i
              id="cross-left"
              class="fa-solid fa-circle-xmark"
              v-if="!CorrectMailAddress && MailAddress"
            ></i>
          </div>
        </div>
        <div class="city">
          <label for="city">City/Locality</label><br />
          <select name="city" id="locality" class="bg-blue-50 shadow-md border-none text-base pr-8" v-model="city">
            <option value="gujarat">Gujarat</option>
            <option value="Delhi">Delhi</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="6">6</option>
            <option value="7">7</option>
            <option value="8">8</option>
            <option value="9">9</option>
            <option value="10">10</option>
            <option value="11">11</option>
            <option value="12">12</option>
            <option value="13">13</option>
            <option value="14">14</option>
            <option value="15">15</option>
          </select>
        </div>
      </div>
      <div class="row-three">
        <div class="country">
          <label for="country">Country</label><br />
          <select name="country" id="select-country" class="bg-blue-50 shadow-md border-none text-base pr-8" v-model="country">
            <option value="india">India</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="6">6</option>
            <option value="7">7</option>
            <option value="8">8</option>
            <option value="9">9</option>
            <option value="10">10</option>
            <option value="11">11</option>
            <option value="12">12</option>
            <option value="13">13</option>
            <option value="14">14</option>
            <option value="15">15</option>
          </select>
        </div>
        <div class="contact-telephone">
          <label for="phone">Contact Telephone</label><br />
          <div class="contact-telephone-input" >
            <input type="tel" id="phone" class="bg-blue-50 shadow-md border-none text-base pr-8" name="phone" pattern="[\d\s\(\)+\-]*" v-model="ContactTelephone" @input="ValidateContactTelephone" placeholder="E.g., +1 (555) 123-4567"/>
            <i
              class="fa-solid fa-circle-check"
              id="tick-right"
              v-if="CorrectContactTelephone && ContactTelephone"
            ></i>
            <i
              id="cross-right"
              class="fa-solid fa-circle-xmark"
              v-if="!CorrectContactTelephone && ContactTelephone"
            ></i>
          </div>
        </div>
      </div>
      <div class="row-four">
        <div class="fax-number">
          <label for="fax" >Contact Fax</label><br />
          <div class="fax-number-input" >
            <input type="tel" id="fax" class="bg-blue-50 shadow-md border-none text-base pr-8" name="phone" pattern="[\d\s\(\)+\-]*" v-model="FaxNumber" @input="ValidateFaxNumber" placeholder="E.g., +1 (555) 123-4567"/>
            <i
              class="fa-solid fa-circle-check"
              id="tick-left"
              v-if="CorrectFaxNumber && FaxNumber"
            ></i>
            <i
              id="cross-left"
              class="fa-solid fa-circle-xmark"
              v-if="!CorrectFaxNumber && FaxNumber"
            ></i>
          </div>
        </div>
        <div class="contact-email">
          <label for="email">Contact Email</label><br />
          <div class="email-input " >
            <input type="email" id="email" class="bg-blue-50 shadow-md border-none text-base pr-8" name="email" v-model="email" @input="ValidateEmail" placeholder="example@example.com"/>
            <i
              class="fa-solid fa-circle-check"
              id="tick-right"
              v-if="CorrectEmail && email"
            ></i>
            <i
              id="cross-right"
              class="fa-solid fa-circle-xmark"
              v-if="!CorrectEmail && email"
            ></i>
          </div>
        </div>
      </div>
    </div>
    
  </div>
</template>

<script>
  import { ref, watch } from "vue";
import useValidate from "@vuelidate/core";
export default {
   setup(props, { emit }) {
    const country = ref('');
    const city = ref('')
    const ContactPerson = ref('');
    const CorrectContactPerson= ref(false);
    const organization = ref('');
    const CorrectOrganization = ref(false);
    const MailAddress = ref('');
    const CorrectMailAddress = ref(false);
    const ContactTelephone = ref('');
    const CorrectContactTelephone = ref(false);
    const FaxNumber = ref('');
    const CorrectFaxNumber = ref(false);
    const email = ref('');
    const CorrectEmail = ref(false);
    const v$ = useValidate();

    const handleRightClick = () =>{
      // const { emit } = getCurrentInstance(); // Access emit function using getCurrentInstance
      // Emit an event to the parent component to validate and proceed
      // Ensure that the necessary data is filled
      
        // Emit an event to the parent component
        // This event is caught in the parent component to proceed to the next step
        console.log('emiting');
        const data = {
        country: country.value,
        city: city.value,
        ContactPerson: ContactPerson.value,
        ContactTelephone: ContactTelephone.value,
        CorrectContactPerson: CorrectContactPerson.value,
        CorrectContactTelephone: CorrectContactTelephone.value,
        organization: organization.value,
        CorrectOrganization: CorrectOrganization.value,
        MailAddress: MailAddress.value,
        CorrectMailAddress: CorrectMailAddress.value,
        FaxNumber: FaxNumber.value,
        CorrectFaxNumber: CorrectFaxNumber.value,
        
      };
      // Emit the 'update-data' event with the updated data
      emit("update-data", data);
        emit('validate-and-proceed-form-three');
        console.log(city.value)
      
    };

    const handleLeftClick = () => {
      emit('MoveBackToTwo');
    }

    const ValidateContactPerson= ()=>{
      CorrectContactPerson.value = ContactPerson.value.length >= 4 && ContactPerson.value.length < 101;
    } 

    const ValidateOrganization= ()=>{
      CorrectOrganization.value = organization.value.length >= 2 && organization.value.length < 101;
    } 

    const ValidateMailAddress= ()=>{
      CorrectMailAddress.value = MailAddress.value.length >= 3 && MailAddress.value.length < 101;
    } 

    const ValidateContactTelephone= ()=>{
      const ContactTelephonePattern = /^[\d\s()+-]*$/;
      CorrectContactTelephone.value = ContactTelephone.value.length >= 3 && ContactTelephone.value.length < 16 && ContactTelephonePattern.test(ContactTelephone.value);
    } 

    const ValidateFaxNumber = () => {
      const faxNumberPattern = /^[\d\s()+-]*$/;
      CorrectFaxNumber.value = faxNumberPattern.test(FaxNumber.value) && FaxNumber.value.length>=3 && FaxNumber.value.length<=15;
    };

    const ValidateEmail= () =>{
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      CorrectEmail.value = emailPattern.test(email.value);
    }


    



    return {
      v$,
      CorrectContactPerson,
      ContactPerson,
      CorrectOrganization,
      organization,
      CorrectMailAddress,
      MailAddress,
      ContactTelephone,
      CorrectContactTelephone,
      CorrectEmail,
      email,
      FaxNumber,
      handleLeftClick,
      CorrectFaxNumber,
      ValidateContactPerson,
      ValidateOrganization,
      ValidateMailAddress,
      ValidateFaxNumber,
      ValidateContactTelephone,
      ValidateEmail,
      handleRightClick,
      city,
      country,
    };
  }
  };
</script>

<style scoped>
.body {
  padding: 0;
  margin: 0;
}



.bottom-layer {
  width: 100%;
  padding: 1em;
  text-align: center;
  font-size: 1.5em;
  
  display: flex;
  gap: 0.5rem;
  justify-content: center;
}

#right {
  transform: rotate(180deg);
  margin-left: 8%;
}

.fax-number-input, .contact-person-input,.organization-input,.mailing-address-input,.contact-telephone-input,.email-input{
  position: relative;
}



.row-one,
.row-two,
.row-three,
.row-four {
  display: flex;
  justify-content: space-evenly;
  gap: 3em;
}

.heading {
  margin-right: 18em;
}



#cross-left{
 position: absolute;
 right: 6%;
 margin-top: 0.7em;
 color: crimson;
}

#cross-right{
  position: absolute;
   right: 6%;
  margin-top: 0.7em;
  color: crimson;

}

#tick-left{
 position: absolute;
 right: 6%;
 margin-top: 12px;
 color: green;
}

#tick-right{
  position: absolute;
 right: 6%;
 margin-top: 12px;
  color: green;
}

input {
  /* Gradient fill */
  color: #344747;
  font-size: 1em;
  border: none;
  border-radius: 50px;
  width: 13rem;
  height: 2.5rem;
  font-style: italic;
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2);
  text-indent: 0.5em;
  
  box-sizing: border-box;
 
}

select {
   /* Gradient fill */
  color: #344747;
  
  border: none;
  border-radius: 50px;
  width: 13rem;
  height: 2.5rem;
  font-style: italic;
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2);
  text-indent: 1em;
  font-weight: 300;
  box-sizing: border-box;
  
}

/* Base styles */

/* Styles for small phones (portrait and landscape) */
  /* Media Queries */
@media screen and (max-width: 640px) {
  /* Small mobile devices */
  .white{
    width: 100%;
  }
  .form-container-three{
    margin-left: 8.5rem;
  }
  h3{
    
    position: relative;
    
  }
  .row-one,.row-four,.row-three,.row-two{
    flex-direction: column;
    gap: 1rem;
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
