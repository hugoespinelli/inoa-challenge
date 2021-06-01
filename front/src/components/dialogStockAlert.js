import React from "react";
import Button from '@material-ui/core/Button';
import PropTypes from 'prop-types';
import NumberFormat from 'react-number-format';
import TextField from '@material-ui/core/TextField';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';

import { ALERT_ACTIONS } from "../constants";

export default function DialogStockAlert({action, open, handleClose, onClick}) {
 
  const [price, setprice] = React.useState(action.stock.price / 100);

  const handleChange = (value) => {
    setprice(value);
  };

  return (
        <Dialog
          open={open}
          onClose={handleClose}
          aria-labelledby="form-dialog-title"
        >
          <DialogTitle id="form-dialog-title">Alerta de {action.action}</DialogTitle>
          <DialogContent>
            <DialogContentText>
              Insira o valor que deseja emitir o alerta para a {action.action}.
            </DialogContentText>
            <TextField
              autoFocus
              margin="dense"
              id="price"
              label="Preço ação"
              value={price}
              onChange={handleChange}
              fullWidth
              InputProps={{
                inputComponent: NumberFormatCustom,
              }}
            />
          </DialogContent>
          <DialogActions>
            <Button onClick={handleClose} color="primary">
              Cancel
            </Button>
            <Button onClick={() => onClick(action, price)} color="primary">
             {action.action}
            </Button>
          </DialogActions>
        </Dialog>
  );
}

DialogStockAlert.propTypes = {
  open: PropTypes.bool.isRequired,
  action: PropTypes.shape({
    action: PropTypes.oneOf([ALERT_ACTIONS.BUY, ALERT_ACTIONS.SELL]).isRequired
  }),
  handleClose: PropTypes.func.isRequired,
  onClick: PropTypes.func.isRequired,
};


function NumberFormatCustom(props) {
  const { inputRef, onChange, ...other } = props;

  return (
    <NumberFormat
      {...other}
      getInputRef={inputRef}
      onValueChange={(values) => {
        onChange(values.value);
      }}
      prefix="R$"
      decimalScale={2}
      decimalSeparator={','}
      fixedDecimalScale
      isNumericString
      allowedDecimalSeparators={[',']}
    />
  );
}

NumberFormatCustom.propTypes = {
  inputRef: PropTypes.func.isRequired,
  name: PropTypes.string.isRequired,
  onChange: PropTypes.func.isRequired,
};