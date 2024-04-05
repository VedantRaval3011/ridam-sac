<template>
  <div class=" flex bg-gradient-to-b from-blue-300 to-blue-200 overflow-hidden flex-col h-screen w-screen">
    <div class="flex justify-between p-4">
      <div class="flex items-center">
        <img src="../../../assets/vedas.png" alt="vedas logo"  class=" w-28  h-auto"/>
      </div>
      <div class="flex items-center">
        
        <img class="w-16 h-auto" src="../../../assets/userbg.png" alt="user-image" />
      </div>
    </div>
    <div class="flex justify-center items-center mt-16 space-x-16">
        <div class="btn-back ">
          <button class="py-2 px-4 bg-blue-500 hover:bg-blue-600 text-white font-semibold rounded-lg shadow-md focus:outline-none" @click="$router.push('/ridam')">Back</button>
        </div>
        <div class="heading">

        <h1 class=" font-semibold">Primary Data Management</h1>
        
        <input type="text" v-model="searchQuery" placeholder="Search..." /> 
        </div>
        <div class="add-button">
            <button class="py-2 px-4 bg-blue-500 hover:bg-blue-600 text-white font-semibold rounded-lg shadow-md focus:outline-none" @click="$router.push('/primary-data-management')">Add data</button>
        </div>
    </div>
    <div class="table-container">
      <div class="scrollable-table">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Name of Dataset</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            
            <!-- Rows will be dynamically added here -->
            <tr v-for="row in filteredRows" :key="row.id">
              <td>{{ row.id }}</td>
              <td>{{ row.name }}</td>
              <td><button @click="editRow(row)">Edit</button></td>
            </tr> 
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['id'],
  data() {
    return {
      searchQuery: '',
      rows: [
        
        // Add more rows as needed
      ]
    };
    },
  computed: {
    filteredRows() {
      return this.rows.filter(row => row.name.toLowerCase().includes(this.searchQuery.toLowerCase()));
    }
  },
  created() {
    this.getAllData(); // Call the method to fetch data when the component is created
    
  },
  methods: {
    getAllData() {
      fetch('http://192.168.2.220:8001/view') 
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          // Update rows data with fetched data
          this.rows = data;
        })
        .catch(error => {
          console.error('There was a problem with the fetch operation:', error);
        });
    },
    editRow(row) {
      // Fetch data for the selected row from the backend API
      const id = row.id;
       this.$router.push({ name: 'edit', params: { id } });
    }
    }  
}
</script>

<style scoped>
   

.scrollable-table {
  overflow-y: auto;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: 20px;
}

table {
  width: 75%;
  border-collapse: collapse;
  background-color: transparent;
}

thead th {
  background-color: #eee;
}

tbody tr:nth-child(even) {
  background-color: #f2f2f2;
}

tbody tr:nth-child(odd) {
  background-color: #ddd;
}

td,
th {
  padding: 10px;
}

.input-container {
  margin-top: 10px;
}

input[type="text"] {
  padding: 8px;
  padding: 8px 18px 8px 18px;
  border-radius: 4px;
  border: 1px solid #ccc;
  width: 100%;
}





@media screen and (max-width: 640px) {
  /* Small mobile devices */
  .add-button button{
    position: relative;
    right: 1rem;
  }
  .btn-back{
    position: relative;
    left: 1rem;
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