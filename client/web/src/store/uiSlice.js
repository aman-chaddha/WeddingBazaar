import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  step: 0,
  theme: 'light',
}

const uiSlice = createSlice({
  name: 'ui',
  initialState,
  reducers: {
    nextStep(state) {
      state.step += 1
    },
    resetSteps(state) {
      state.step = 0
    },
    setTheme(state, action) {
      state.theme = action.payload
    },
  },
})

export const { nextStep, resetSteps, setTheme } = uiSlice.actions
export default uiSlice.reducer
