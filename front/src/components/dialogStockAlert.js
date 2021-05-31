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

export default function DialogStockAlert({action, open, handleClose, onClick}) {

  const [values, setValues] = React.useState(1320);

  const handleChange = (value) => {
    console.log(value)
    setValues(value);
  };

  return (
        <Dialog
          open={open}
          onClose={handleClose}
          aria-labelledby="form-dialog-title"
        >
          <DialogTitle id="form-dialog-title">Alerta de {action}</DialogTitle>
          <DialogContent>
            <DialogContentText>
              Insira o valor que deseja emitir o alerta para a {action}.
            </DialogContentText>
            <TextField
              autoFocus
              margin="dense"
              id="price"
              label="Preço ação"
              value={values}
              onChange={handleChange}
              fullWidth
              InputProps={{
                inputComponent: NumberFormatCustom,
              }}
            />
          </DialogContent>
          <DialogActions>
            <Button onClick={onClick} color="primary">
              Cancel
            </Button>
            <Button onClick={onClick} color="primary">
             {action}
            </Button>
          </DialogActions>
        </Dialog>
  );
}

DialogStockAlert.propTypes = {
  open: PropTypes.bool.isRequired,
  action: PropTypes.string.isRequired,
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