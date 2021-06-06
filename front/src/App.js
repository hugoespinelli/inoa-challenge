import './App.css';
import StockContainer from './container/StockContainer';
import { SnackbarProvider } from 'notistack';
function App() {
  return (
    <div className="App">
      <SnackbarProvider maxSnack={3}>
        <StockContainer />
      </SnackbarProvider>
    </div>
  );
}

export default App;
