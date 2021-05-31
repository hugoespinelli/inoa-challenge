import React from "react";
import Button from '@material-ui/core/Button';
import Container from "@material-ui/core/Container";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import MaterialTable from "material-table";
import TextField from '@material-ui/core/TextField';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import DialogStockAlert from '../components/dialogStockAlert';

export default function StockContainer() {
  const [modalOpen, setModalOpen] = React.useState(false);
  const [action, setAction] = React.useState("");

  const handleOpen = (rowData, action) => {
    setModalOpen(true);
    setAction(action);
  };

  const handleClose = () => {
    setModalOpen(false);
  };

  return (
    <React.Fragment>
      <Container fluid style={{ backgroundColor: "#e7e7e7" }}>
        <DialogStockAlert
          open={modalOpen}
          handleClose={handleClose}
          action={action}
          onClick={() => console.log("compra")}
        />
        <Grid container spacing={4}>
          <Grid item md={6}>
            <MaterialTable
              title="Tabela de ações"
              localization={{
                pagination: {
                  labelDisplayedRows: "{from}-{to} até {count}",
                  labelRowsSelect: "linhas",
                },
                toolbar: {
                  searchPlaceholder: "Procurar ação",
                },
                header: {
                  actions: "Alertas",
                },
                body: {
                  emptyDataSourceMessage: "Sem ações disponíveis",
                },
              }}
              columns={[
                { title: "Código", field: "code" },
                { title: "Preço", field: "price" },
              ]}
              data={[
                { code: "PETR4", price: 1990 },
                { code: "BTG11", price: 10123 },
              ]}
              actions={[
                {
                  icon: "add_alert",
                  iconProps: { color: "primary" },
                  tooltip: "Alerta de Compra",
                  onClick: (event, rowData) => handleOpen(rowData, "Compra"),
                },
                (rowData) => ({
                  icon: "add_alert",
                  iconProps: { color: "error" },
                  tooltip: "Alerta de Venda",
                  onClick: (event, rowData) => handleOpen(rowData, "Venda"),
                }),
              ]}
              options={{
                actionsColumnIndex: -1,
              }}
            />
          </Grid>

          <Grid item md={6}>
            <MaterialTable
              title="Tabela de alerta de ações"
              localization={{
                pagination: {
                  labelDisplayedRows: "{from}-{to} até {count}",
                  labelRowsSelect: "linhas",
                },
                toolbar: {
                  searchPlaceholder: "Procurar ação",
                },
                header: {
                  actions: "Ações",
                },
                body: {
                  emptyDataSourceMessage: "Sem ações disponíveis",
                },
              }}
              columns={[
                { title: "Código", field: "code" },
                { title: "Preço", field: "price" },
                { title: "Alerta de preço", field: "price_alert" },
              ]}
              data={[
                { code: "PETR4", price: 1990, price_alert: 1880 },
                { code: "BTG11", price: 10123, price_alert: 10022 },
              ]}
              actions={[
                {
                  icon: "edit",
                  tooltip: "Editar",
                  onClick: (event, rowData) =>
                    alert("You saved " + rowData.name),
                },
                (rowData) => ({
                  icon: "delete",
                  tooltip: "Deletar",
                  onClick: (event, rowData) =>
                    console.log("You want to delete " + rowData.name),
                  disabled: rowData.birthYear < 2000,
                }),
              ]}
              options={{
                actionsColumnIndex: -1,
              }}
            />
          </Grid>
        </Grid>
      </Container>
    </React.Fragment>
  );
}
