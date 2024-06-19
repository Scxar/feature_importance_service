import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useDashboardStore = defineStore('dashboard', () => {
  const chartIdCounter=ref(0)
  const view = ref('local')
  const nestedView = ref('')
  const datasetColumns = ref(null)
  const sidebarFormData = ref(null)
  const model = ref('xdg');
  const dataset = ref('kaggle_heart_disease_2020');

  function getChartId() {
    let tempId=chartIdCounter.value
    chartIdCounter.value = tempId + 1;
    console.log(tempId)
    return 'chart-'+tempId;
  }

  return {view, sidebarFormData, datasetColumns, nestedView, model, dataset,getChartId}
})
