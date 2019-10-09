<template>
  <div class="scene-finder">
    <h1>{{ title }}</h1>
  </div>
</template>

<script>
export default {
  components: [],
  props: [],
  data() {
    return {
      title: 'Scene Finder',
    };
  },
  computed: {},
  mounted() {},
  methods: {
    fetchScenes() {
      console.log('fetchScenes');
    },
  },
};
</script>

<style scoped>
@media screen and (max-width: 480px) {
}
</style>
