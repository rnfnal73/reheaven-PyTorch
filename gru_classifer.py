#new Classifier
class BiGRU(ElectraForSequenceClassification):
  def __init__(self,config):
    super(self).__init__(config)

    self.gru = nn.GRU(input_size=256,hidden_size=768,num_layers=1,bias=True,bidirectional=True,batch_first=True)
    self.fc == nn.Linear(number_of_hidden,num of class)

  def forward(
          self,
          input_ids=None,
          attention_mask=None,
          token_type_ids=None,
          position_ids=None,
          head_mask=None,
          inputs_embeds=None,
          labels=None,
          output_attentions=None,
          output_hidden_states=None,
          return_dict=None,
    ):
          return_dict = return_dict if return_dict is not None else self.config.use_return_dict

          discriminator_hidden_states_1 = self.electra(
              input_ids,
              attention_mask,
              token_type_ids,
              position_ids,
              head_mask,
              inputs_embeds,
              output_attentions,
              output_hidden_states,
              return_dict,
          )
          tmp_output = self.gru()
          discriminator_hidden_states = self.fc(tmp_output)
          sequence_output = discriminator_hidden_states[0]
          logits = self.classifier(sequence_output)

          loss = None
          if labels is not None:
              if self.num_labels == 1:
                  #  We are doing regression
                  loss_fct = MSELoss()
                  loss = loss_fct(logits.view(-1), labels.view(-1))
              else:
                  loss_fct = CrossEntropyLoss()
                  loss = loss_fct(logits.view(-1, self.num_labels), labels.view(-1))

          if not return_dict:
              output = (logits,) + discriminator_hidden_states[1:]
              return ((loss,) + output) if loss is not None else output

          return SequenceClassifierOutput(
              loss=loss,
              logits=logits,
              hidden_states=discriminator_hidden_states.hidden_states,
              attentions=discriminator_hidden_states.attentions,
          )