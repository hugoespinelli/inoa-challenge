import React from "react";
import Container from "@material-ui/core/Container";
import { useSnackbar } from 'notistack';
import Grid from "@material-ui/core/Grid";
import MaterialTable from "material-table";
import DialogStockAlert from "../components/dialogStockAlert";

import StockApi from "../logic/stockApi";
import { ALERT_ACTIONS } from "../constants";

export default function StockContainer() {
  const [modalOpen, setModalOpen] = React.useState(false);
  const [action, setAction] = React.useState({
    stock: {},
    action: "",
  });
  const { enqueueSnackbar } = useSnackbar();
  const alertTableRef = React.createRef();

  const handleOpen = (rowData, newAction) => {
    setModalOpen(true);
    setAction({
      stock: rowData,
      action: newAction,
    });
  };

  const handleClose = () => {
    setModalOpen(false);
  };

  const renderDialog = () => {
    return modalOpen ? (
      <DialogStockAlert
        open={modalOpen}
        handleClose={handleClose}
        action={action}
        onClick={handleActionModal}
      />
    ) : (
      <></>
    );
  };

  const handleActionModal = async (action, price) => {
    try {
      await StockApi.createAlert(action.stock.id, price * 100, action.action);
      enqueueSnackbar('Alerta criado com sucesso!', {variant: 'success'});
      alertTableRef.current.onQueryChange()
    } catch(e) {
      enqueueSnackbar('Falha ao criar o alerta.', {variant: 'error'});
    } finally{
      handleClose();
    }
  };

  async function paginate(promiseResult) {
    const {data} = await promiseResult;
    return {
      data: data,
      page: 0,
      totalCount: data.length, 
      count: data.length, 
    }
  }

  return (
    <React.Fragment>
      <Container>
        {renderDialog()}
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
              data={() => paginate(StockApi.list())}
              actions={[
                {
                  icon: "add_alert",
                  iconProps: { color: "primary" },
                  tooltip: "Alerta de Compra",
                  onClick: (event, rowData) => handleOpen(rowData, ALERT_ACTIONS.BUY),
                },
                (rowData) => ({
                  icon: "add_alert",
                  iconProps: { color: "error" },
                  tooltip: "Alerta de Venda",
                  onClick: (event, rowData) => handleOpen(rowData, ALERT_ACTIONS.SELL),
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
              tableRef={alertTableRef}
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
                { title: "Alerta de preço", field: "price_alert" },
                { title: "Operação", field: "type" },
              ]}
              data={() => paginate(StockApi.listAlert())}
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
