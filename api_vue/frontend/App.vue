<template>
  <div style="padding: 2rem; font-family: sans-serif;">
    <h2>Buscar Operadora</h2>
    <input v-model="termo" @input="buscar" placeholder="Digite um nome..." style="padding: 0.5rem; width: 300px;" />
    <ul v-if="operadoras.length">
      <li v-for="op in operadoras" :key="op.codigo_registro">
        {{ op.nome_fantasia }}
      </li>
    </ul>
    <p v-else-if="termo">Nenhum resultado encontrado.</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      termo: '',
      operadoras: []
    };
  },
  methods: {
    async buscar() {
      const res = await fetch(`http://localhost:5000/buscar?q=${this.termo}`);
      this.operadoras = await res.json();
    }
  }
}
</script>
