<template>
    <div class="auth">
        <div class="login" v-if="restore"> 
          <h1 class="text-center">Optovka.kz</h1>
          <form>
              <v-text-field
                  v-model="name"
                  :error-messages="nameErrors"
                  :counter="20"
                  label="Логин"
                  required
                  @input="$v.name.$touch()"
                  @blur="$v.name.$touch()"
              ></v-text-field>
              <v-text-field
                  v-model="password"
                  :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                  :rules="[rules.required, rules.min]"
                  :type="show ? 'text' : 'password'"
                  name="input-10-1"
                  label="Пароль"
                  hint="At least 8 characters"
                  counter
                  @click:append="show = !show"
              ></v-text-field>
              <v-btn class="mr-4" @click="submit"> Войти </v-btn>
              <v-btn @click="restorePass"> Восстановить пароль </v-btn>
          </form>
        </div>
        <div class="restore" v-else>
          <h1 class="text-center">Optovka.kz</h1>
          <h3 class="text-center">Восстановить пароль</h3>
          <form>
              <v-text-field
                  v-model="name"
                  :error-messages="nameErrors"
                  :counter="20"
                  label="Логин"
                  required
                  @input="$v.name.$touch()"
                  @blur="$v.name.$touch()"
              ></v-text-field>
              <v-btn class="mr-4" @click="restorePass"> Восстановить пароль </v-btn>
          </form>
        </div>
    </div>
</template>

<script>
import { validationMixin } from 'vuelidate'
import { required, maxLength, email } from 'vuelidate/lib/validators'

export default {
  mixins: [validationMixin],
  validations: {
    name: { required, maxLength: maxLength(10) },
    email: { required, email }
  },
  name: 'Auth',
  data () {
    return {
      name: '',
      password: '',
      show: false,
      rules: {
        required: value => !!value || 'Required.',
        min: v => v.length >= 4 || 'Min 4 characters',
        emailMatch: () => ('The email and password you entered don\'t match')
      },
      restore: false
    }
  },
  computed: {
    nameErrors () {
      const errors = []
      if (!this.$v.name.$dirty) return errors
      !this.$v.name.maxLength && errors.push('Name must be at most 10 characters long')
      !this.$v.name.required && errors.push('Name is required.')
      return errors
    },
    emailErrors () {
      const errors = []
      if (!this.$v.email.$dirty) return errors
      !this.$v.email.email && errors.push('Must be valid e-mail')
      !this.$v.email.required && errors.push('E-mail is required')
      return errors
    }
  },
  created() {
  },
  methods: {
    submit () {
      fetch('http://127.0.0.1:8000/auth/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: this.name, password: this.password })
      })
      .then(resp => resp.json())
      .then(res => {
        if (res.token) {
          this.$store.commit('setAuth', true)
          this.$cookies.set('opt-token', res.token, '30d')
          this.$cookies.set('opt-id', res.id, '30d')
          this.$router.push('/')
        }
		  })
      .catch(error => console.log('error', error))
    },
    clear () {
      this.$v.$reset()
      this.name = ''
      this.password = ''
    },
    restorePass() {
      console.log('here')
      this.restore = !this.restore
    }
  }
}
</script>
