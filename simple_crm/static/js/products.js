$(document).ready(function() {
	$('#cbx_editions').click(function() {
		var checked = $(this).is(':checked');
		if (checked) {
			$('#editions').show();
		} else {
			$('#editions').hide();
		}
	});
	$('#btn_add_new_editions').click(function() {
		var html = '<div class="row">    <div class="form-group col-md-3">		<label class="control-label">Name</label>		<input class="form-control" maxlength="50" name="editions_name" type="text" />	</div>    <div class="form-group col-md-3">		<label class="control-label">Perpetual</label>		<input class="form-control" maxlength="50" name="editions_perpetual" type="number" step="0.1" value="0" />	</div>    <div class="form-group col-md-3">		<label class="control-label">Monthly Price</label>		<input class="form-control"  maxlength="50" name="editions_monthly_price" type="number" step="0.1" value="0" />	</div>    <div class="form-group col-md-3">		<label class="control-label">Yearly Price</label>		<input class="form-control"  maxlength="50" name="editions_yearly_price" type="number" step="0.1" value="0" />	</div></div>';
		$('#editions').prepend($(html));
	})
});